# import numpy as np
# import pandas as pd
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, LeakyReLU
# from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
# from sklearn.model_selection import train_test_split, KFold
# from sklearn.preprocessing import StandardScaler, LabelEncoder, PowerTransformer, RobustScaler
# from sklearn.ensemble import VotingClassifier
# from sklearn.feature_selection import SelectKBest, f_classif
# from imblearn.over_sampling import SMOTE
# from imblearn.combine import SMOTEENN
# import xgboost as xgb
# from sklearn.metrics import accuracy_score
# import numpy as np
# import joblib

# # Load data
# data = pd.read_csv('crop_dataset.csv')
# target_column = 'Crop'

# # Separate features and labels
# X = data.drop(columns=[target_column])
# y = data[target_column]

# # Enhanced feature engineering
# def create_interaction_features(X):
#     numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns
#     for i in range(len(numeric_cols)):
#         for j in range(i+1, len(numeric_cols)):
#             col1, col2 = numeric_cols[i], numeric_cols[j]
#             X[f'{col1}_{col2}_ratio'] = X[col1] / (X[col2] + 1e-6)
#             X[f'{col1}_{col2}_product'] = X[col1] * X[col2]
#     return X

# # Apply feature engineering
# X = create_interaction_features(X)

# # Categorical encoding (converting categorical columns to numeric)
# categorical_cols = X.select_dtypes(include=['object']).columns
# for col in categorical_cols:
#     X[col] = X[col].astype('category').cat.codes  # Convert to numeric using category codes

# # Feature selection
# selector = SelectKBest(score_func=f_classif, k='all')
# X_selected = selector.fit_transform(X, y)
# selected_features_mask = selector.get_support()
# selected_feature_names = X.columns[selected_features_mask].tolist()

# # Save selected features
# print(f"Selected features: {selected_feature_names}")
# joblib.dump(selected_feature_names, 'selected_features.pkl')

# # Advanced preprocessing
# def preprocess_features(X):
#     power_transformer = PowerTransformer(method='yeo-johnson')
#     robust_scaler = RobustScaler()
    
#     # Apply both transformers
#     X_power = power_transformer.fit_transform(X)
#     X_robust = robust_scaler.fit_transform(X_power)
    
#     # Save the trained transformers
#     joblib.dump(power_transformer, 'power_transformer.pkl')
#     joblib.dump(robust_scaler, 'robust_scaler.pkl')

#     return X_robust

# X = preprocess_features(X)

# # Enhanced sampling
# smote_enn = SMOTEENN(random_state=42)
# X_resampled, y_resampled = smote_enn.fit_resample(X, y)

# # Encode crop labels BEFORE resampling
# label_encoder = LabelEncoder()
# y_encoded = label_encoder.fit_transform(y)  # Convert crops to numerical labels

# # Save the encoder for later use in inference
# joblib.dump(label_encoder, 'label_encoder.pkl')

# # Apply SMOTEENN on encoded labels
# X_resampled, y_resampled = smote_enn.fit_resample(X, y_encoded)
  

# # Define deep learning model
# def create_deep_model(input_shape, num_classes):
#     inputs = keras.Input(shape=input_shape)
    
#     # First block with skip connection
#     x = Dense(512, kernel_regularizer=keras.regularizers.l2(0.01))(inputs)
#     x = LeakyReLU(negative_slope=0.1)(x)
#     x = BatchNormalization()(x)
#     x = Dropout(0.5)(x)
    
#     skip1 = x
    
#     # Second block
#     x = Dense(256, kernel_regularizer=keras.regularizers.l2(0.01))(x)
#     x = LeakyReLU(negative_slope=0.1)(x)
#     x = BatchNormalization()(x)
#     x = Dropout(0.4)(x)
    
#     # Add skip connection
#     x = keras.layers.Concatenate()([x, skip1])
    
#     # Third block
#     x = Dense(128, kernel_regularizer=keras.regularizers.l2(0.01))(x)
#     x = LeakyReLU(negative_slope=0.1)(x)
#     x = BatchNormalization()(x)
#     x = Dropout(0.3)(x)
    
#     # Output
#     outputs = Dense(num_classes, activation='softmax')(x)
    
#     return keras.Model(inputs, outputs)

# # Create ensemble of models
# def create_ensemble(input_shape, num_classes, n_models=3):
#     models = []
    
#     for i in range(n_models):
#         # Deep learning model
#         dl_model = create_deep_model(input_shape, num_classes)
#         dl_model.compile(
#             optimizer=keras.optimizers.Adam(learning_rate=0.001),
#             loss='sparse_categorical_crossentropy',
#             metrics=['accuracy']
#         )
#         models.append(dl_model)
        
#         # XGBoost model
#         xgb_model = xgb.XGBClassifier(
#             learning_rate=0.01,
#             n_estimators=200,
#             max_depth=7,
#             min_child_weight=1,
#             gamma=0.1,
#             subsample=0.8,
#             colsample_bytree=0.8,
#             objective='multi:softprob',
#             num_class=num_classes,
#             random_state=42+i
#         )
#         models.append(xgb_model)
    
#     return models

# # Training with k-fold cross validation
# n_splits = 5
# kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# # Callbacks for deep learning models
# early_stopping = EarlyStopping(
#     monitor='val_accuracy',
#     patience=20,
#     restore_best_weights=True,
#     min_delta=0.001
# )

# reduce_lr = ReduceLROnPlateau(
#     monitor='val_accuracy',
#     factor=0.2,
#     patience=10,
#     min_lr=1e-6,
#     min_delta=0.001,
#     verbose=1
# )

# # Train ensemble
# def train_ensemble(X, y, input_shape, num_classes):
#     ensemble_predictions = []
#     fold_accuracies = []
    
#     for fold, (train_idx, val_idx) in enumerate(kf.split(X)):
#         print(f"\nTraining Fold {fold + 1}/{n_splits}")
        
#         X_train, X_val = X[train_idx], X[val_idx]
#         y_train, y_val = y[train_idx], y[val_idx]
        
#         # Create and train models for this fold
#         models = create_ensemble(input_shape, num_classes)
#         fold_predictions = []
        
#         for i, model in enumerate(models):
#             if isinstance(model, keras.Model):
#                 # Train deep learning model
#                 model.fit(
#                     X_train, y_train,
#                     validation_data=(X_val, y_val),
#                     epochs=100,
#                     batch_size=32,
#                     callbacks=[early_stopping, reduce_lr],
#                     verbose=1
#                 )
#                 pred = model.predict(X_val)
#                 fold_predictions.append(pred)
#             else:
#                 # Train XGBoost model
#                 model.fit(X_train, y_train)
#                 pred = model.predict_proba(X_val)
#                 fold_predictions.append(pred)
        
#         # Average predictions for this fold
#         fold_pred = np.mean(fold_predictions, axis=0)
#         fold_pred_classes = np.argmax(fold_pred, axis=1)
#         fold_accuracy = accuracy_score(y_val, fold_pred_classes)
#         fold_accuracies.append(fold_accuracy)
#         print(f"Fold {fold + 1} Accuracy: {fold_accuracy:.4f}")
        
#         ensemble_predictions.append((val_idx, fold_pred))
    
#     return ensemble_predictions, np.mean(fold_accuracies)

# # Train the ensemble
# input_shape = (X_resampled.shape[1],)
# num_classes = len(np.unique(y_encoded))
# ensemble_predictions, mean_accuracy = train_ensemble(X_resampled, y_encoded, input_shape, num_classes)

# print(f"\nMean Cross-Validation Accuracy: {mean_accuracy:.4f}")

# # Save predictions and actual values
# final_predictions = np.zeros((len(X_resampled), num_classes))
# for idx, pred in ensemble_predictions:
#     final_predictions[idx] = pred

# # Final evaluation
# final_pred_classes = np.argmax(final_predictions, axis=1)
# final_accuracy = accuracy_score(y_encoded, final_pred_classes)
# print(f"Final Ensemble Accuracy: {final_accuracy:.4f}")

# # Save the best model from the ensemble
# best_model = create_deep_model(input_shape, num_classes)
# best_model.compile(
#     optimizer=keras.optimizers.Adam(learning_rate=0.001),
#     loss='sparse_categorical_crossentropy',
#     metrics=['accuracy']
# )
# best_model.fit(
#     X_resampled, y_encoded,
#     epochs=100,
#     batch_size=32,
#     callbacks=[early_stopping, reduce_lr],
#     validation_split=0.2,
#     verbose=1
# )
# best_model.save('best_crop_model.keras')


import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, LeakyReLU
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, LabelEncoder, PowerTransformer, RobustScaler
from sklearn.feature_selection import SelectKBest, f_classif
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTEENN
import xgboost as xgb
from sklearn.metrics import accuracy_score
import joblib

# Load data
data = pd.read_csv('crop_dataset.csv')
target_column = 'Crop'

# Separate features and labels
X = data.drop(columns=[target_column])
y = data[target_column]

# Encode crop labels BEFORE resampling
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Convert crops to numerical labels
joblib.dump(label_encoder, 'label_encoder.pkl')  # Save encoder for inference

# Enhanced feature engineering
def create_interaction_features(X):
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns
    for i in range(len(numeric_cols)):
        for j in range(i+1, len(numeric_cols)):
            col1, col2 = numeric_cols[i], numeric_cols[j]
            X[f'{col1}_{col2}_ratio'] = X[col1] / (X[col2] + 1e-6)
            X[f'{col1}_{col2}_product'] = X[col1] * X[col2]
    return X

# Apply feature engineering
X = create_interaction_features(X)

# Categorical encoding (converting categorical columns to numeric)
categorical_cols = X.select_dtypes(include=['object']).columns
for col in categorical_cols:
    X[col] = X[col].astype('category').cat.codes  # Convert to numeric using category codes

# Feature selection
selector = SelectKBest(score_func=f_classif, k='all')
X_selected = selector.fit_transform(X, y_encoded)
selected_features_mask = selector.get_support()
selected_feature_names = X.columns[selected_features_mask].tolist()
joblib.dump(selected_feature_names, 'selected_features.pkl')  # Save selected features

# Advanced preprocessing
def preprocess_features(X):
    power_transformer = PowerTransformer(method='yeo-johnson')
    robust_scaler = RobustScaler()
    X_power = power_transformer.fit_transform(X)
    X_robust = robust_scaler.fit_transform(X_power)
    joblib.dump(power_transformer, 'power_transformer.pkl')
    joblib.dump(robust_scaler, 'robust_scaler.pkl')
    return X_robust

X = preprocess_features(X)

# Enhanced sampling (use SMOTE instead of SMOTEENN to prevent class loss)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y_encoded)

# Verify class distribution
print("Original encoded classes:", np.unique(y_encoded))
print("After resampling:", np.unique(y_resampled))

# Define deep learning model
def create_deep_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    x = Dense(512, kernel_regularizer=keras.regularizers.l2(0.01))(inputs)
    x = LeakyReLU(negative_slope=0.1)(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    skip1 = x
    x = Dense(256, kernel_regularizer=keras.regularizers.l2(0.01))(x)
    x = LeakyReLU(negative_slope=0.1)(x)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)
    x = keras.layers.Concatenate()([x, skip1])
    x = Dense(128, kernel_regularizer=keras.regularizers.l2(0.01))(x)
    x = LeakyReLU(negative_slope=0.1)(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    outputs = Dense(num_classes, activation='softmax')(x)
    return keras.Model(inputs, outputs)

# Train deep learning model
input_shape = (X_resampled.shape[1],)
num_classes = len(np.unique(y_resampled))
model = create_deep_model(input_shape, num_classes)
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Callbacks
early_stopping = EarlyStopping(monitor='val_accuracy', patience=20, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_accuracy', factor=0.2, patience=10, min_lr=1e-6, verbose=1)

# Train model
model.fit(
    X_resampled, y_resampled,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping, reduce_lr],
    verbose=1
)

# Save best model
model.save('best_crop_model.keras')
print("Model training complete and saved.")



# import numpy as np
# import pandas as pd
# import tensorflow as tf
# from tensorflow.keras import layers, Model, regularizers
# from tensorflow.keras.optimizers import Nadam
# from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
# from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
# from sklearn.preprocessing import StandardScaler, LabelEncoder, PowerTransformer, QuantileTransformer
# from sklearn.feature_selection import RFECV, SelectKBest, f_classif, mutual_info_classif
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, balanced_accuracy_score
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.decomposition import PCA
# from imblearn.combine import SMOTEENN
# from imblearn.over_sampling import SMOTE, ADASYN
# import xgboost as xgb
# import joblib
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# import collections

# # Create directory for saving visualizations
# os.makedirs('visualizations', exist_ok=True)

# # Load data
# data = pd.read_csv('crop_dataset.csv')
# target_column = 'Crop'

# # ================== DATA VISUALIZATION FUNCTIONS ==================
# def plot_feature_distributions(data, target_column):
#     numeric_cols = data.select_dtypes(include=['number']).columns
#     for col in numeric_cols:
#         if col != target_column:
#             plt.figure(figsize=(10, 6))
#             sns.boxplot(x=target_column, y=col, data=data)
#             plt.xticks(rotation=90)
#             plt.title(f'Distribution of {col} by Crop Type')
#             plt.tight_layout()
#             plt.savefig(f'visualizations/{col}_distribution.png')
#             plt.close()

# def plot_correlation_matrix(X):
#     plt.figure(figsize=(12, 10))
#     corr_matrix = X.corr()
#     mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
#     sns.heatmap(corr_matrix, mask=mask, cmap='coolwarm', annot=False, 
#                 square=True, linewidths=.5, cbar_kws={"shrink": .5})
#     plt.title('Feature Correlation Matrix')
#     plt.tight_layout()
#     plt.savefig('visualizations/correlation_matrix.png')
#     plt.close()

# # ================== NUMERICALLY STABLE FEATURE ENGINEERING ==================
# def create_interaction_features(X):
#     numeric_cols = X.select_dtypes(include=['number']).columns
    
#     # Clip values based on percentiles to handle extreme values
#     for col in numeric_cols:
#         lower = X[col].quantile(0.01)
#         upper = X[col].quantile(0.99)
#         X[col] = X[col].clip(lower, upper)
        
#     # Create interaction features with numerical stability
#     for i in range(len(numeric_cols)):
#         for j in range(i+1, len(numeric_cols)):
#             col1, col2 = numeric_cols[i], numeric_cols[j]
            
#             # Safe logarithmic interaction with epsilon
#             X[f'{col1}_log_{col2}'] = (
#                 np.log1p(np.abs(X[col1])) + 1e-6
#             ) * (
#                 np.log1p(np.abs(X[col2])) + 1e-6
#             )
            
#             # Bounded exponential interaction
#             exp_input = np.clip(X[col1] + X[col2], -5, 5)
#             X[f'{col1}_exp_{col2}'] = np.exp(exp_input) / 1e4
            
#     # Domain-specific features with numerical safety
#     if all(col in X.columns for col in ['N', 'P', 'K']):
#         X['NPK_balance'] = (X['N'] + X['P']) / (X['K'].clip(lower=1e-3) + 1e-6)
#         X['nutrient_score'] = X[['N', 'P', 'K']].clip(0, 100).dot([0.3, 0.4, 0.3])
        
#     if 'temperature' in X.columns and 'humidity' in X.columns:
#         X['temp_humidity_index'] = (
#             X['temperature'].clip(-20, 50) * 
#             (1 + (X['humidity'].clip(0, 100) - 50) / 100)
#         )
        
#     return X.replace([np.inf, -np.inf], np.nan).fillna(0)

# # ================== ROBUST FEATURE SELECTION ==================
# def select_features_advanced(X, y):
#     try:
#         # Initial filtering of constant features
#         constant_features = X.columns[X.nunique() == 1]
#         X_filtered = X.drop(columns=constant_features)
        
#         # Stabilize data before feature selection
#         preprocessor = AdvancedPreprocessor()
#         X_processed = preprocessor.fit_transform(X_filtered)
        
#         # Ensure finite values
#         X_processed = np.nan_to_num(X_processed, nan=0, posinf=np.finfo(np.float32).max, neginf=np.finfo(np.float32).min)
        
#         # Use simpler model for feature selection
#         rf = RandomForestClassifier(
#             n_estimators=50,
#             max_depth=3,
#             random_state=42,
#             n_jobs=-1
#         )
#         selector = RFECV(rf, step=1, cv=3, scoring='accuracy', min_features_to_select=10)
        
#         selector.fit(X_processed, y)
#         selected_features = X_filtered.columns[selector.support_]
        
#         return X_filtered[selected_features], selected_features.tolist()
    
#     except Exception as e:
#         print(f"Feature selection failed: {str(e)}")
#         print("Using all non-constant features as fallback")
#         return X_filtered, X_filtered.columns.tolist()

# # ================== IMPROVED PREPROCESSOR ==================
# class AdvancedPreprocessor:
#     def __init__(self):
#         self.scalers = {}
#         self.transformers = {}
#         self.clip_bounds = {}
        
#     def fit_transform(self, X):
#         X_processed = X.copy()
        
#         for col in X.columns:
#             # Store original distribution stats
#             self.clip_bounds[col] = (
#                 X[col].quantile(0.01),
#                 X[col].quantile(0.99)
#             )
            
#             # Initial clipping
#             X_processed[col] = X_processed[col].clip(*self.clip_bounds[col])
            
#             # Handle NaNs and infinities
#             X_processed[col] = np.nan_to_num(
#                 X_processed[col], 
#                 nan=X[col].median(),
#                 posinf=self.clip_bounds[col][1],
#                 neginf=self.clip_bounds[col][0]
#             )
            
#             # Power transform with regularization
#             pt = PowerTransformer(method='yeo-johnson', standardize=False)
#             X_processed[col] = pt.fit_transform(X_processed[[col]].values.reshape(-1, 1))
#             self.transformers[col] = pt
            
#             # Robust scaling
#             scaler = StandardScaler()
#             X_processed[col] = scaler.fit_transform(X_processed[[col]].values.reshape(-1, 1))
#             self.scalers[col] = scaler
            
#             # Final clipping to prevent extreme scaling artifacts
#             X_processed[col] = X_processed[col].clip(-5, 5)
            
#         return X_processed.values

# # ================== NUMERICALLY STABLE MODEL ARCHITECTURE ==================
# def create_advanced_model(input_shape, num_classes):
#     inputs = tf.keras.Input(shape=input_shape)
    
#     # Feature normalization layer
#     x = layers.LayerNormalization()(inputs)
    
#     # Attention mechanism with bounded activation
#     attention = layers.Dense(input_shape[0], activation='sigmoid')(x)
#     x = layers.Multiply()([x, attention])
    
#     # Bottleneck with gradient clipping
#     x = layers.Dense(128, activation='swish', 
#                     kernel_regularizer=regularizers.l1_l2(1e-4, 1e-3),
#                     kernel_constraint=tf.keras.constraints.MaxNorm(3))(x)
#     x = layers.BatchNormalization()(x)
#     x = layers.Dropout(0.3)(x)
    
#     # Residual blocks with gradient control
#     for units in [256, 512, 256]:
#         residual = layers.Dense(units)(x)
#         x = layers.Dense(units, activation='swish', 
#                         kernel_constraint=tf.keras.constraints.MaxNorm(2))(x)
#         x = layers.BatchNormalization()(x)
#         x = layers.Dropout(0.2)(x)
#         x = layers.add([x, residual])
    
#     # Temperature-scaled output
#     outputs = layers.Dense(num_classes, activation='softmax')(x)
#     outputs = layers.Lambda(lambda x: x / 0.7)(outputs)
    
#     model = Model(inputs, outputs)
    
#     # Optimizer with gradient clipping
#     optimizer = Nadam(
#         learning_rate=0.0005,
#         weight_decay=1e-4,
#         clipnorm=1.0
#     )
    
#     model.compile(
#         optimizer=optimizer,
#         loss=FocalLoss(),
#         metrics=['accuracy'],
#         weighted_metrics=['accuracy']
#     )
    
#     return model

# # ================== STABLE FOCAL LOSS IMPLEMENTATION ==================
# class FocalLoss(tf.keras.losses.Loss):
#     def __init__(self, alpha=0.25, gamma=2.0, name="focal_loss"):
#         super().__init__(name=name)
#         self.alpha = alpha
#         self.gamma = gamma

#     def call(self, y_true, y_pred):
#         y_pred = tf.clip_by_value(y_pred, 1e-7, 1.0 - 1e-7)
#         ce = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
#         pt = tf.exp(-ce)
#         return tf.reduce_mean(self.alpha * (1 - pt)**self.gamma * ce)

# # ================== SIMPLE HYPERPARAMETER TUNING ==================
# def tune_hyperparameters(X_train, y_train):
#     print("Performing simplified hyperparameter tuning...")
    
#     # Define a set of hyperparameters to try
#     learning_rates = [0.0001, 0.001, 0.01]
#     activations = ['relu', 'swish']
#     units_options = [64, 128, 256]
#     batch_sizes = [16, 32, 64]
    
#     best_val_accuracy = 0
#     best_params = {}
#     best_model = None
    
#     # Split data for validation
#     X_tune, X_val, y_tune, y_val = train_test_split(
#         X_train, y_train, test_size=0.2, stratify=y_train, random_state=42
#     )
    
#     # Try each combination and track the best
#     for lr in learning_rates:
#         for activation in activations:
#             for units in units_options:
#                 for batch_size in batch_sizes:
#                     print(f"Trying: lr={lr}, activation={activation}, units={units}, batch_size={batch_size}")
                    
#                     # Create and train a model with these parameters
#                     model = tf.keras.Sequential([
#                         layers.Dense(units, activation=activation, input_shape=(X_tune.shape[1],)),
#                         layers.BatchNormalization(),
#                         layers.Dropout(0.3),
#                         layers.Dense(units // 2, activation=activation),
#                         layers.BatchNormalization(),
#                         layers.Dropout(0.2),
#                         layers.Dense(len(np.unique(y_tune)), activation='softmax')
#                     ])
                    
#                     model.compile(
#                         optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
#                         loss='sparse_categorical_crossentropy',
#                         metrics=['accuracy']
#                     )
                    
#                     # Use early stopping for efficiency
#                     early_stop = EarlyStopping(
#                         monitor='val_accuracy',
#                         patience=5,
#                         restore_best_weights=True
#                     )
                    
#                     # Train for a small number of epochs
#                     history = model.fit(
#                         X_tune, y_tune,
#                         epochs=20,
#                         batch_size=batch_size,
#                         validation_data=(X_val, y_val),
#                         callbacks=[early_stop],
#                         verbose=0
#                     )
                    
#                     # Get the best validation accuracy
#                     val_accuracy = max(history.history['val_accuracy'])
                    
#                     if val_accuracy > best_val_accuracy:
#                         best_val_accuracy = val_accuracy
#                         best_params = {
#                             'learning_rate': lr,
#                             'activation': activation,
#                             'units': units,
#                             'batch_size': batch_size
#                         }
#                         best_model = model
    
#     print(f"Best parameters: {best_params}")
#     print(f"Best validation accuracy: {best_val_accuracy:.4f}")
    
#     return best_model

# # ================== MAIN WORKFLOW WITH ERROR HANDLING ==================
# try:
#     # Load and prepare data
#     data = pd.read_csv('crop_dataset.csv')
#     X = data.drop(columns=[target_column])
#     y = data[target_column]

#     # Feature engineering
#     X = create_interaction_features(X)
#     print("Feature engineering completed. Shape:", X.shape)

#     # Encode labels
#     label_encoder = LabelEncoder()
#     y_encoded = label_encoder.fit_transform(y)
#     class_names = label_encoder.classes_
#     joblib.dump(label_encoder, 'label_encoder.pkl')

#     # Feature selection
#     X_selected, selected_features = select_features_advanced(X, y_encoded)
#     print("Selected features:", len(selected_features))
#     joblib.dump(selected_features, 'selected_features.pkl')

#     # Preprocessing
#     preprocessor = AdvancedPreprocessor()
#     X_processed = preprocessor.fit_transform(X_selected)
#     print("Preprocessing completed. Max value:", np.max(X_processed))

#     # Check class distribution
#     class_counts = collections.Counter(y_encoded)
#     print("Class distribution before balancing:", class_counts)
    
#     # Filter out classes with only 1 sample
#     min_samples_per_class = 2
#     rare_classes = [class_id for class_id, count in class_counts.items() if count < min_samples_per_class]
    
#     if rare_classes:
#         print(f"WARNING: Removing {len(rare_classes)} rare classes with fewer than {min_samples_per_class} samples.")
#         mask = np.array([y_val not in rare_classes for y_val in y_encoded])
#         X_processed = X_processed[mask]
#         y_encoded = y_encoded[mask]
#         # Remap class labels to ensure they are consecutive integers starting from 0
#         unique_classes = np.unique(y_encoded)
#         class_mapping = {old_label: i for i, old_label in enumerate(unique_classes)}
#         y_encoded = np.array([class_mapping[label] for label in y_encoded])
#         print(f"After removing rare classes, {len(np.unique(y_encoded))} classes remain.")
    
#     # Class balancing with adaptive strategy
#     print("Class counts after filtering:", collections.Counter(y_encoded))
    
#     # Use a more robust strategy for class balancing
#     try:
#         # Try SMOTE first
#         smote = SMOTE(random_state=42, k_neighbors=min(5, min(collections.Counter(y_encoded).values())-1))
#         X_res, y_res = smote.fit_resample(X_processed, y_encoded)
#         print("SMOTE class balancing completed.")
#     except Exception as e:
#         print(f"SMOTE failed: {str(e)}. Trying alternative method...")
#         try:
#             # Try ADASYN with adaptive k_neighbors
#             adasyn = ADASYN(random_state=42, n_neighbors=min(5, min(collections.Counter(y_encoded).values())-1))
#             X_res, y_res = adasyn.fit_resample(X_processed, y_encoded)
#             print("ADASYN class balancing completed.")
#         except Exception as e2:
#             print(f"ADASYN failed: {str(e2)}. Using original data with sampling weights.")
#             # Fall back to using original data with class weights
#             X_res, y_res = X_processed, y_encoded
            
#     print("Class balancing completed. New shape:", X_res.shape)
#     print("New class distribution:", collections.Counter(y_res))

#     # Split data
#     X_train, X_test, y_train, y_test = train_test_split(
#         X_res, y_res, test_size=0.2, stratify=y_res, random_state=42
#     )

#     # Hyperparameter tuning - use simplified approach
#     print("Starting hyperparameter tuning...")
#     best_model = tune_hyperparameters(X_train, y_train)

#     # Train final model
#     print("Training final model...")
#     final_model = create_advanced_model((X_train.shape[1],), len(np.unique(y_res)))
    
#     # Calculate class weights for imbalanced data
#     class_weights = {i: len(y_train) / (len(np.unique(y_train)) * np.sum(y_train == i)) 
#                     for i in np.unique(y_train)}
    
#     history = final_model.fit(
#         X_train, y_train,
#         epochs=200,
#         batch_size=32,
#         validation_split=0.2,
#         class_weight=class_weights,
#         callbacks=[
#             EarlyStopping(patience=25, restore_best_weights=True),
#             ReduceLROnPlateau(factor=0.2, patience=15),
#             ModelCheckpoint('best_checkpoint.keras', save_best_only=True)
#         ],
#         verbose=1
#     )

#     # Evaluate
#     y_pred = np.argmax(final_model.predict(X_test), axis=1)
#     print(f"\nFinal Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
#     print(f"Balanced Accuracy: {balanced_accuracy_score(y_test, y_pred):.4f}")
#     print(classification_report(y_test, y_pred, target_names=[str(class_names[i]) for i in np.unique(y_res)]))

#     # Plot training history
#     plt.figure(figsize=(12, 4))
#     plt.subplot(1, 2, 1)
#     plt.plot(history.history['accuracy'])
#     plt.plot(history.history['val_accuracy'])
#     plt.title('Model Accuracy')
#     plt.ylabel('Accuracy')
#     plt.xlabel('Epoch')
#     plt.legend(['Train', 'Validation'], loc='upper left')
    
#     plt.subplot(1, 2, 2)
#     plt.plot(history.history['loss'])
#     plt.plot(history.history['val_loss'])
#     plt.title('Model Loss')
#     plt.ylabel('Loss')
#     plt.xlabel('Epoch')
#     plt.legend(['Train', 'Validation'], loc='upper left')
#     plt.tight_layout()
#     plt.savefig('visualizations/training_history.png')
    
#     # Save model
#     final_model.save('best_crop_model.keras')
#     print("Model saved successfully.")

# except Exception as e:
#     print(f"\nError in workflow: {str(e)}")
#     print("Check data preprocessing steps and numerical stability")
#     import traceback
#     traceback.print_exc()
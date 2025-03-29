# import pandas as pd
# import numpy as np

# # Define soil nutrient thresholds and fertilizer recommendations
# fertilizer_rules = [
#     {"nutrient": "N", "min": 0, "max": 20, "fertilizer": "Blood Meal", "amount_range": (50, 100)},
#     {"nutrient": "N", "min": 20, "max": 40, "fertilizer": "Cow Manure", "amount_range": (100, 150)},
#     {"nutrient": "P", "min": 0, "max": 10, "fertilizer": "Bone Meal", "amount_range": (100, 200)},
#     {"nutrient": "P", "min": 10, "max": 20, "fertilizer": "Chicken Manure", "amount_range": (150, 250)},
#     {"nutrient": "K", "min": 0, "max": 50, "fertilizer": "Greensand", "amount_range": (50, 150)},
#     {"nutrient": "K", "min": 50, "max": 80, "fertilizer": "Compost", "amount_range": (100, 200)},
#     {"nutrient": "pH", "min": 0, "max": 5.5, "fertilizer": "Lime", "amount_range": (200, 500)},
#     {"nutrient": "pH", "min": 7.5, "max": 10, "fertilizer": "Peat Moss", "amount_range": (100, 300)},
#     {"nutrient": "OM", "min": 0, "max": 1.5, "fertilizer": "Compost", "amount_range": (200, 500)},
# ]

# # Function to determine the recommended fertilizer based on soil values
# def recommend_fertilizer(n, p, k, ph, om):
#     for rule in fertilizer_rules:
#         if rule["nutrient"] == "N" and rule["min"] <= n < rule["max"]:
#             return rule["fertilizer"], np.random.randint(*rule["amount_range"])
#         if rule["nutrient"] == "P" and rule["min"] <= p < rule["max"]:
#             return rule["fertilizer"], np.random.randint(*rule["amount_range"])
#         if rule["nutrient"] == "K" and rule["min"] <= k < rule["max"]:
#             return rule["fertilizer"], np.random.randint(*rule["amount_range"])
#         if rule["nutrient"] == "pH" and rule["min"] <= ph < rule["max"]:
#             return rule["fertilizer"], np.random.randint(*rule["amount_range"])
#         if rule["nutrient"] == "OM" and rule["min"] <= om < rule["max"]:
#             return rule["fertilizer"], np.random.randint(*rule["amount_range"])
#     return "No Fertilizer Needed", 0  # Default if no recommendation is found

# # Generate synthetic soil data
# num_samples = 1000  # Number of dataset rows
# data = []

# for _ in range(num_samples):
#     n = np.random.uniform(5, 50)  # Nitrogen range
#     p = np.random.uniform(5, 30)  # Phosphorus range
#     k = np.random.uniform(20, 100)  # Potassium range
#     ph = np.random.uniform(4.5, 8)  # pH range
#     om = np.random.uniform(0.5, 5)  # Organic matter %

#     fertilizer, amount = recommend_fertilizer(n, p, k, ph, om)
    
#     data.append([n, p, k, ph, om, fertilizer, amount])

# # Create DataFrame
# df = pd.DataFrame(data, columns=["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)", "Recommended Fertilizer", "Amount (kg/ha)"])

# # Save dataset to CSV
# df.to_csv("soil_fertilizer_dataset.csv", index=False)

# print("Synthetic soil-fertilizer dataset generated and saved as 'soil_fertilizer_dataset.csv'!")


import pandas as pd
import numpy as np

# Define soil nutrient thresholds and fertilizer recommendations
fertilizer_rules = [
    {"nutrient": "N", "min": 0, "max": 20, "fertilizer": "Blood Meal", "amount_range": (50, 100)},
    {"nutrient": "N", "min": 20, "max": 40, "fertilizer": "Cow Manure", "amount_range": (100, 150)},
    {"nutrient": "N", "min": 40, "max": 60, "fertilizer": "Fish Emulsion", "amount_range": (150, 200)},
    
    {"nutrient": "P", "min": 0, "max": 10, "fertilizer": "Bone Meal", "amount_range": (100, 200)},
    {"nutrient": "P", "min": 10, "max": 20, "fertilizer": "Rock Phosphate", "amount_range": (150, 250)},
    {"nutrient": "P", "min": 20, "max": 40, "fertilizer": "Chicken Manure", "amount_range": (200, 300)},

    {"nutrient": "K", "min": 0, "max": 50, "fertilizer": "Greensand", "amount_range": (50, 150)},
    {"nutrient": "K", "min": 50, "max": 80, "fertilizer": "Compost", "amount_range": (100, 200)},
    {"nutrient": "K", "min": 80, "max": 120, "fertilizer": "Wood Ash", "amount_range": (150, 250)},

    {"nutrient": "pH", "min": 0, "max": 5.5, "fertilizer": "Lime", "amount_range": (200, 500)},
    {"nutrient": "pH", "min": 7.5, "max": 10, "fertilizer": "Peat Moss", "amount_range": (100, 300)},

    {"nutrient": "OM", "min": 0, "max": 1.5, "fertilizer": "Compost", "amount_range": (200, 500)},
    {"nutrient": "OM", "min": 1.5, "max": 3, "fertilizer": "Vermicompost", "amount_range": (150, 400)}
]

# Function to determine the recommended fertilizer
def recommend_fertilizer(n, p, k, ph, om):
    for rule in fertilizer_rules:
        if rule["nutrient"] == "N" and rule["min"] <= n < rule["max"]:
            return rule["fertilizer"], np.random.randint(*rule["amount_range"])
        if rule["nutrient"] == "P" and rule["min"] <= p < rule["max"]:
            return rule["fertilizer"], np.random.randint(*rule["amount_range"])
        if rule["nutrient"] == "K" and rule["min"] <= k < rule["max"]:
            return rule["fertilizer"], np.random.randint(*rule["amount_range"])
        if rule["nutrient"] == "pH" and rule["min"] <= ph < rule["max"]:
            return rule["fertilizer"], np.random.randint(*rule["amount_range"])
        if rule["nutrient"] == "OM" and rule["min"] <= om < rule["max"]:
            return rule["fertilizer"], np.random.randint(*rule["amount_range"])
    return "No Fertilizer Needed", 0

# Generate synthetic soil data
num_samples = 5000  # Increase sample size for better training
data = []

for _ in range(num_samples):
    n = np.random.uniform(5, 60)  # Nitrogen range
    p = np.random.uniform(5, 40)  # Phosphorus range
    k = np.random.uniform(20, 120)  # Potassium range
    ph = np.random.uniform(4.5, 8)  # pH range
    om = np.random.uniform(0.5, 5)  # Organic matter %

    fertilizer, amount = recommend_fertilizer(n, p, k, ph, om)
    
    data.append([n, p, k, ph, om, fertilizer, amount])

# Create DataFrame
df = pd.DataFrame(data, columns=["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)", "Recommended Fertilizer", "Amount (kg/ha)"])

# Save dataset
df.to_csv("soil_fertilizer_dataset.csv", index=False)
print("✅ Synthetic dataset generated: 'soil_fertilizer_dataset.csv'!")

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
<<<<<<< HEAD
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
=======
    # Solid Fertilizers
    {
        "name": "FFJ Fermented Plant",
        "type": "solid",
        "nutrients": {"N": "high", "K": "medium"},
        "soil_conditions": {
            "pH": {"min": 5.5, "max": 7.0},
            "OM": {"min": 1.0, "max": 3.0}
        },
        "amount_range": (2, 4),  # kg per square meter
        "application_frequency": "monthly"
    },
    {
        "name": "FFJ Fermented Juice Plant",
        "type": "solid",
        "nutrients": {"N": "medium", "P": "medium", "K": "high"},
        "soil_conditions": {
            "pH": {"min": 5.5, "max": 7.5},
            "OM": {"min": 1.5, "max": 4.0}
        },
        "amount_range": (1, 3),  # kg per square meter
        "application_frequency": "bi-weekly"
    },
    {
        "name": "Vermi Compost",
        "type": "solid",
        "nutrients": {"N": "medium", "P": "high", "K": "medium"},
        "soil_conditions": {
            "pH": {"min": 6.0, "max": 7.5},
            "OM": {"min": 0.5, "max": 3.0}
        },
        "amount_range": (3, 5),  # kg per square meter
        "application_frequency": "quarterly"
    },
    {
        "name": "Organic Compost",
        "type": "solid",
        "nutrients": {"N": "medium", "P": "medium", "K": "medium"},
        "soil_conditions": {
            "pH": {"min": 5.5, "max": 8.0},
            "OM": {"min": 0.5, "max": 5.0}
        },
        "amount_range": (2, 4),
        "application_frequency": "monthly"
    },
    {
        "name": "Blood Meal",
        "type": "solid",
        "nutrients": {"N": "high", "P": "low", "K": "low"},
        "soil_conditions": {
            "pH": {"min": 6.0, "max": 7.5},
            "OM": {"min": 1.0, "max": 4.0}
        },
        "amount_range": (1, 2),
        "application_frequency": "monthly"
    },
    
    # Liquid Fertilizers
    {
        "name": "OHN Calpus",
        "type": "liquid",
        "nutrients": {"N": "low", "P": "low", "K": "low"},
        "soil_conditions": {
            "pH": {"min": 6.0, "max": 7.0}
        },
        "amount_range": (1, 2),  # liters per square meter
        "application_frequency": "weekly"
    },
    {
        "name": "Wound Vinegar",
        "type": "liquid",
        "nutrients": {"N": "low", "P": "low", "K": "low"},
        "soil_conditions": {
            "pH": {"min": 5.5, "max": 7.0}
        },
        "amount_range": (0.5, 1),  # liters per square meter
        "application_frequency": "bi-weekly"
    },
    {
        "name": "Calcium Phosphate",
        "type": "liquid",
        "nutrients": {"P": "high", "Ca": "high"},
        "soil_conditions": {
            "pH": {"min": 6.0, "max": 7.5}
        },
        "amount_range": (1, 2),  # liters per square meter
        "application_frequency": "monthly"
    },
    {
        "name": "Fish Emulsion",
        "type": "liquid",
        "nutrients": {"N": "high", "P": "medium", "K": "low"},
        "soil_conditions": {
            "pH": {"min": 5.5, "max": 7.5}
        },
        "amount_range": (0.5, 1.5),
        "application_frequency": "bi-weekly"
    },
    {
        "name": "Seaweed Extract",
        "type": "liquid",
        "nutrients": {"N": "low", "P": "low", "K": "high"},
        "soil_conditions": {
            "pH": {"min": 5.0, "max": 8.0}
        },
        "amount_range": (0.5, 1),
        "application_frequency": "weekly"
    }
]

def recommend_fertilizer(soil_data, crop_type=None):
    """
    Recommend fertilizers based on soil conditions and crop type
    soil_data: dict containing soil parameters (N, P, K, pH, OM)
    crop_type: string indicating the recommended crop (optional)
    """
    recommendations = []
    
    # Default to medium organic matter if not provided
    if "OM" not in soil_data:
        soil_data["OM"] = 2.0
    
    # Check each fertilizer against soil conditions
    for fertilizer in fertilizer_rules:
        is_suitable = True
        
        # Check soil pH conditions
        if "pH" in fertilizer["soil_conditions"]:
            ph_range = fertilizer["soil_conditions"]["pH"]
            if not (ph_range["min"] <= soil_data["pH"] <= ph_range["max"]):
                is_suitable = False
        
        # Check organic matter conditions if available
        if "OM" in fertilizer["soil_conditions"] and "OM" in soil_data:
            om_range = fertilizer["soil_conditions"]["OM"]
            if not (om_range["min"] <= soil_data["OM"] <= om_range["max"]):
                is_suitable = False
        
        if is_suitable:
            amount = np.random.uniform(*fertilizer["amount_range"])
            recommendations.append({
                "type": fertilizer["type"],
                "name": fertilizer["name"],  # Always use the predefined name
                "amount": round(amount, 2),
                "unit": "kg/m²" if fertilizer["type"] == "solid" else "L/m²",
                "frequency": fertilizer["application_frequency"]
            })
    
    # If no recommendations found, return a default organic compost recommendation
    if not recommendations:
        return [{
            "type": "solid",
            "name": "Organic Compost",  # Default fallback option
            "amount": 2.0,
            "unit": "kg/m²",
            "frequency": "monthly"
        }]
    
    return recommendations

# Generate synthetic soil data
num_samples = 5000
data = []

for _ in range(num_samples):
    # Generate soil parameters
    soil_data = {
        "N": np.random.uniform(5, 60),
        "P": np.random.uniform(5, 40),
        "K": np.random.uniform(20, 120),
        "pH": np.random.uniform(4.5, 8),
        "OM": np.random.uniform(0.5, 5)
    }
    
    # Simulate a crop recommendation (you'll replace this with your actual crop ML model)
    crop_type = np.random.choice(["Rice", "Corn", "Vegetables", "Fruits"])
    
    # Get fertilizer recommendations
    recommendations = recommend_fertilizer(soil_data, crop_type)
    
    # Store the data
    data.append({
        "Nitrogen (mg/kg)": soil_data["N"],
        "Phosphorus (mg/kg)": soil_data["P"],
        "Potassium (mg/kg)": soil_data["K"],
        "pH": soil_data["pH"],
        "Organic Matter (%)": soil_data["OM"],
        "Crop Type": crop_type,
        "Fertilizer Recommendations": recommendations
    })

# Create DataFrame
df = pd.DataFrame(data)
>>>>>>> cy

# Save dataset
df.to_csv("soil_fertilizer_dataset.csv", index=False)
print("✅ Synthetic dataset generated: 'soil_fertilizer_dataset.csv'!")

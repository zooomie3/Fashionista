# Integrating the data using code
# Role: person 3. outfit engine engineer
# Name: outfit_engineer.py


import random
import pandas as pd
def build_outfit(filtered_df, temperature):
    outfit_items = [] #define later
    required_types = ["top", "bottoms", "layers", "shoes"] #where should layers be and difference with outerwear
    optional_types = ["accessoires", "bags", "hats", "outerwear"]

# Handle layering items (if applicable)
    if temperature <= 10: #might change temperature scales later, this is an example!
        required_types.append("outerwear")

    if temperature > 25:
        if "outerwear" in optional_types:
            optional_types.remove("outerwear")

    if weather_condition == "rainy": #how to code this?
        required_types.append("raincoat")
        required_types.append("rainboots")


# Required categories
for clothing_type in required_types:
    items_of_type = filtered_df[filtered_df["type"] == clothing_type]
    if items_of_type.empty:
        print(f"No {clothing_type} available for the occasion!")
        return None # cannot build a valid outfit
    

# Randomly select ONE item
    selected_item = items_of_type.sample(1)
    outfit_items.append(selected_item)

# Handle optional categories
for clothing_type in optional_types:
    items_of_type = filtered_df[filtered_df["type"] == clothing_type]
    if not items_of_type.empty:
        selected_item = items_of_type.sample(1)
        outfit_items.append(selected_item)

# Combine selected items into a one outfit/dataframe
final_outfit = pd.concat(outfit_items, ignore_index=True)
return final_outfit

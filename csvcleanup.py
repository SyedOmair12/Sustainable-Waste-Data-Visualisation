import numpy as np
import pandas as pd

csv_name = "data_sources/country_level_data_0.csv"
waste = pd.read_csv(csv_name)

# Select columns that we are interested in
w = waste[["iso3c","country_name","gdp", "composition_food_organic_waste_percent",
    "composition_glass_percent", "composition_metal_percent",
    "composition_other_percent", "composition_paper_cardboard_percent",
    "composition_plastic_percent", "composition_rubber_leather_percent",
    "composition_wood_percent",
    "composition_yard_garden_green_waste_percent",
    "total_msw_total_msw_generated_tons_year"]]

# Drop rows with missing data
gdpw = w.dropna(subset=["gdp"])
msww = w.dropna(subset=["total_msw_total_msw_generated_tons_year"])

# Combine the two data frames, drop the duplicate rows and sort
combined = gdpw.append(msww).drop_duplicates().sort_index()

# Output to a new CSV file
combined.to_csv(path_or_buf="cleaned.csv", index=False)

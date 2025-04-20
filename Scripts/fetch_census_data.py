from census import Census
import pandas as pd

API_KEY = "YOUR-API-KEY-GOES-HERE"
# Initialize Census API with your key
c = Census(API_KEY)

# Fetch data for all ZIP Code Tabulation Areas (ZCTA)
data = c.acs5.get(
    ("NAME", "B19013_001E", "B15003_022E", "B01003_001E", "B23025_005E"),
    {"for": "zip code tabulation area:*"}  # "*" fetches all ZCTAs
)

# Convert to DataFrame
census_df = pd.DataFrame(data)

# Rename columns
census_df.rename(columns={
    "B19013_001E": "MEDIAN_INCOME",
    "B15003_022E": "BACHELORS_PERCENT",
    "B01003_001E": "POPULATION",
    "B23025_005E": "UNEMPLOYMENT_RATE",
    "zip code tabulation area": "ZIP_CODE"
}, inplace=True)

# Save to CSV
census_df.to_csv("census_acs_2022.csv", index=False)
import pandas as pd

library_df = pd.read_csv("..\Raw_Data\PLS_FY22_AE_pud22i.csv")

library_df["ZIP_CODE"] = (
    library_df["ZIP"]
    .astype(str)
    .str.zfill(5)
)

library_df = library_df.drop(columns=['ZIP', 'ZIP4', 'ZIP_M', 'ZIP4_M'])


census_df = pd.read_csv("..\Raw_Data\census_acs_2022.csv")

census_df["ZIP_CODE"] = (
    census_df["ZIP_CODE"]
    .str.extract(r'(\d{5})')[0]
)

census_df = census_df.drop(columns=['NAME'])

merged_df = pd.merge(
    library_df,
    census_df,
    on='ZIP_CODE',
    how='inner',
    suffixes=('_LIB', '_CENSUS')
)

merged_df.to_csv("merged_data.csv", index=False)






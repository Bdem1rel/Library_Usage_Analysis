import pandas as pd

library_df = pd.read_csv("../Datasets/Raw_Data/PLS_FY22_AE_pud22i.csv", encoding='ISO-8859-1')

library_df["ZIP-CODE"] = (
    library_df["ZIP"]
    .astype(str)
    .str.zfill(5)
)

library_df = library_df.drop(columns=['ZIP', 'ZIP4', 'ZIP_M', 'ZIP4_M'])


census_df = pd.read_csv("../Datasets/Raw_Data/census_acs_2022.csv")

census_df["ZIP-CODE"] = (
    census_df["ZIP_CODE"]
    .astype(str)
    .str.zfill(5)
)

census_df = census_df.drop(columns=['NAME', 'ZIP_CODE'])

merged_df = pd.merge(
    library_df,
    census_df,
    on='ZIP-CODE',
    how='inner',
    suffixes=('_LIB', '_CENSUS')
)

merged_df.to_csv("../Datasets/Merged_Data/merged_data.csv", index=False)
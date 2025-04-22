# Library Usage & Community Demographics Analysis  
**DSA 210 Spring 2024 Term Project**  

---

## **Motivation**  
Public libraries serve as critical community resources, offering free access to education, technology, and cultural programs. However, library engagement—such as book checkouts or event attendance—varies widely across neighborhoods. These disparities often reflect underlying socioeconomic factors like income levels, education, and population density. By analyzing library usage alongside demographic data, we can uncover patterns that guide fair resource distribution and advocate for data-driven policy decisions.  

This project focuses on answering two key questions:  
1. **How do community demographics correlate with library engagement metrics (e.g., checkouts, program attendance)?**  
2. **Can we predict library usage patterns using socioeconomic indicators?** 

---

## **Data Sources**  
### **1. Library Usage Data**  
- **Source**: [IMLS Public Library Survey (2022)](https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey)  
- **Key Features**:  
  - `TOTCIR`: Total circulation of materials
  - `VISITS`: Total annual library visits 
  - `REGBOR`: Number of registered users   
  - `TOTSTAFF`: Total paid FTE employees
  - `GPTERMS`: Internet computers used by the general public
  - `HRS_OPEN`: Total annual public service hours for all service outlets
  - `TOTPRO`: Total number of synchronous program sessions
  - `TOTATTEN`: Total attendance at synchronous programs
  - `TOTINCM`: Total operating revenue
  - `TOTOPEXP`: Total operating expenditures 
  - `POPU_UND`: Unduplicated population of the legal service area for the library  
  - `ZIP_CODE`: Administrative ZIP code of the library system  

### **2. Community Demographics Data**  
- **Source**: [US Census ACS 5-Year Estimates (2022)](https://www.census.gov/data/developers/data-sets/acs-5year.html)  
- **Key Features**:  
  - `MEDIAN_INCOME`: Median household income by ZIP Code Tabulation Area (ZCTA)  
  - `BACHELORS_PERCENT`: Percentage of population with a bachelor’s degree or higher  
  - `UNEMPLOYMENT_RATE`: Unemployment rate  
  - `ZIP_CODE`: ZIP code 
  
---

## **Data Collection**  
1. **IMLS Data**:  
   - Downloaded the `PLS_FY22_AE_pud22i.csv` file from the IMLS website.  
   - Filtered columns to retain `ZIP_CODE`, `TOTCIR`, `VISITS`, `REGBOR`, `TOTSTAFF`, `TOTATTEN`, `TOTPRO`, `GPTERMS`, `TOTINCM`, `TOTOPEXP`, `HRS_OPEN`, `POPU_UND`.  
   

2. **Census Data**:  
   - **API Integration**: Fetched data using the **US Census Bureau API** (ACS 5-Year Estimates 2022).  
     - **Tools**: Python `census` library with a registered [Census API key](https://api.census.gov/data/key_signup.html).  
     - **Features**: Extracted `B19013_001E` (median income), `B15003_022E` (% bachelor’s degree), and `B23025_005E` (unemployment rate).  
 

---
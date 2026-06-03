import pandas as pd
import requests

# ____________________LIVE NAV FETCH____________________________

# url = "https://api.mfapi.in/mf/125497"

# response = requests.get(url)
# data = response.json()
# nav_df = pd.DataFrame(data['data'])

# # Saving AV history as csv
# nav_df.to_csv(
#     "data/raw/hdfc_top100_nav.csv",
#     index=False
# )
# print("Saved Successfully")


# ____________________FETCHING 5 MUTUAL FUND DETAILS____________________________

# schemes = {
#     "SBI_Bluechip":119551,
#     "ICICI_Bluechip":120503,
#     "Nippon_Large_Cap":118632,
#     "Axis_Bluechip":119092,
#     "Kotak_Bluechip":120841
# }

# for name, code in schemes.items():

#     url = f"https://api.mfapi.in/mf/{code}"

    # response = requests.get(url)

#     data = response.json()

#     df = pd.DataFrame(data['data'])

#     filename = f"data/raw/{name}.csv"

#     df.to_csv(filename, index=False)

#     print(f"{name} saved")

# ____________________EXPLORE FUND MASTER.CSV____________________________

df_fund_master = pd.read_csv("data/raw/01_fund_master.csv")
print("Columns:",df_fund_master.columns)

### Unique Fund Houses
print("\nNo. of unique Fund houses:",df_fund_master['fund_house'].nunique())
print(df_fund_master['fund_house'].unique())


### Categories
print("\nNo. of unique categories:",df_fund_master['category'].nunique())
print(df_fund_master['category'].unique())

### sub-categories
print("\nNo. of unique sub-categories:",df_fund_master['sub_category'].nunique())
print(df_fund_master['sub_category'].unique())

### Risk Grades=]:
print("\nNo. of unique risk category:",df_fund_master['risk_category'].nunique())
print(df_fund_master['risk_category'].unique())

# ____________________VALIDATE AMFI CODES____________________________
# AMFI scheme code uniquely identifies a mutual fund scheme.
# It is used for fetching NAV data through APIs.
print("\nNo. of unique amfi_codes:",df_fund_master['amfi_code'].nunique())

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

missing_codes = set(df_fund_master['amfi_code']) - set(nav_history['amfi_code'])

print("\nMissing Codes:",
    len(missing_codes)
)
# If output Missing Codes: 0 then all codes exist.

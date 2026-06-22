import pandas as pd
import numpy as np

df = pd.read_excel("Dataset for Data Analytics.xlsx")
print(df.head())
print(df.info())
print(df.describe())
# check dataset shape
print("Rows and Columns", df.shape)

# Identify missing values 
print(df.isnull().sum())
print((df.isnull().sum()/len(df))*100)

# Handle missing values
# by filling numericals with mean
df["UnitPrice"]= df["UnitPrice"].fillna(df["UnitPrice"].mean())
df["TotalPrice"]= df["TotalPrice"].fillna(df["TotalPrice"].mean())

# fill text values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print(df.isnull().sum())


# Check Duplicate Records
print("Duplicate Rows:",df.duplicated().sum())
duplicates =df[df.duplicated()]
print(duplicates)

# Remove Duplicaes
df = df.drop_duplicates()

 #Check Duplicate Records
print("Duplicate OrderIDS:",df["OrderID"].duplicated().sum())

# check data types 
print(df.dtypes)

# Correct Data formates
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

 # clean Text columns
text_columns =["CustomerID","Product","ShippingAddress","PaymentMethod","OrderStatus","TrackingNumber","CouponCode",
                 "ReferralSource"
                 ]
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print(df.dtypes)

# verify Numerical columns
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].describe())

# Final validtion 
print("Missing Values:")
print(df.isnull().sum())

print("/nDuplicate Rows:")
print(df.duplicated().sum())

print("/nDuplicate Order IDs:")
print(df["OrderID"].duplicated().sum())


# Cleaned dataset
df.to_excel("Cleaned_Data.xlsx",index=False)


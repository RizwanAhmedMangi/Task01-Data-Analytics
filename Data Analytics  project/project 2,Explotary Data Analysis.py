# Exploratory Data Analysis
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_Data.xlsx")

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())

#calculate Basic Statistics , Mean
print("Average Quantity:",df["Quantity"].mean())
print("Average Unit price:",df["UnitPrice"].mean())
print("Average  Total Price:",df["TotalPrice"].mean())
print("Average Items In Cart:",df["ItemsInCart"].mean())

# calculate Median 
print("Average Quantity:",df["Quantity"].median())
print("Average Unit price:",df["UnitPrice"].median())
print("Average  Total Price:",df["TotalPrice"].median())
print("Average Items In Cart:",df["ItemsInCart"].median())

print(df.count())

 #  Analyse  total Revenue and sales
print("Total Revenue:",df["TotalPrice"].sum())
product_sales = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)
print(product_sales.head(20))

# Visualize Product sales
product_sales.head(20).plot(kind="bar")
plt.title("Top 20 products by sales") 
plt.ylabel("Revenue")
plt.show()

#Analyze Payment Methods
payment = df["PaymentMethod"].value_counts()
print(payment)
payment.plot(kind="pie")
plt.title("Payment Methods")
plt.show()

#Analyze Order Status
status = df["OrderStatus"].value_counts()
print(status)
plt.figure(figsize=(8,6))

colors = ["#4CAF50", "#2196F3", "#FFC107", "#F44336"]  # Green, Blue, Yellow, Red

plt.pie(
    status,
    labels=status.index,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.85,
    wedgeprops={"edgecolor":"white", "linewidth":2}
)

# Create donut hole
centre_circle = plt.Circle((0,0), 0.70, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Order Status Distribution", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()



# Monthly revenue trends
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["TotalPrice"].sum()
print(monthly_sales)

monthly_sales.plot(kind="line",marker="o")
plt.title("Monthly revenue trend")
plt.ylabel("Revenue")
plt.show()

#Identify  outliers 
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR =Q3-Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower) |
    (df["TotalPrice"] > upper)
]
print(outliers)
print("Number of outliers:", len(outliers))
# create Boxplot
plt.boxplot(df["TotalPrice"].dropna())
plt.title("Outlier Detection")
plt.show()

#Analyse customer purchase
customer_sales = df.groupby("CustomerID")["TotalPrice"].sum()
print(customer_sales.sort_values(ascending=False).head(20))

#Correlation Analysis
correlation = df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].corr()
print(correlation)

import matplotlib.pyplot as plt
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)),correlation.columns)
plt.yticks(range(len(correlation.columns)),correlation.columns)
plt.show()


# key observation and findings
print("\nKey  Findings and Observation")
print("1.The dataset contains 1,200 orders and provides information about products, customers, payments, and sales.")
print("2.The total revenue generated from all orders was approximately 1.26 million.")
print("3.Chair and Printer were among the highest revenue-generating products.")
print("4.Some products contributed significantly more revenue than others, indicating varying customer demand.")
print("5.Certain payment methods were used more frequently than others, showing customer payment preferences.")
print("6.Revenue trends varied across different months, suggesting seasonal sales patterns.")
print("7.A small number of transactions were identified as outliers because their TotalPrice values were significantly higher than the majority of orders.")
print("8.Higher quantities purchased generally resulted in higher TotalPrice values.")
print("9.Most orders were concentrated in a few order-status categories.")
print("10.The dataset is suitable for further predictive analytics and business intelligence applications.")


#Save EDA result
product_sales.to_excel("Top_Product_Sales.xlsx")
monthly_sales.to_excel("Monthly_Revenue.xlsx")
outliers.to_excel("Outliers.xlsx")

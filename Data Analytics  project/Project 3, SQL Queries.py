import pandas as pd
import sqlite3

df = pd.read_excel("Cleaned_Data.xlsx")
conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace",index=False)
print("Database Created Successfully")

query = """SELECT * 
            FROM sales
             LIMIT 10"""
print(pd.read_sql(query,conn))

 # basic select Query
query ="""SELECT * FROM sales"""
print(pd.read_sql(query,conn))

# select Specific columns
query = """SELECT OrderID,Product,TotalPrice
             FROM sales;"""
print(pd.read_sql(query,conn))
print(df.head())


#Select total orders
query = """SELECT COUNT(*) AS Total_Orders
             FROM sales;"""
print(pd.read_sql(query,conn))

# Total Revenue
query = """SELECT SUM(TotalPrice) AS Total_Revenue
             FROM sales;"""
print(pd.read_sql(query,conn))

# Calculate Average  Orders value
query = """SELECT AVG(TotalPrice) AS Average_order_value
             FROM sales;"""
print(pd.read_sql(query,conn))

#WHERE clause 
query = """SELECT *
             FROM sales
             WHERE TotalPrice >1000;"""
print(pd.read_sql(query,conn))

# Filter Specific product
query = """SELECT *
             FROM sales
             WHERE Product IN ('Chair', 'Monitor', 'Phone') ;"""
print(pd.read_sql(query,conn))

# ORDERBY Revenue
query = """SELECT Product,TotalPrice
             FROM sales
             ORDER BY TotalPrice DESC;"""
print(pd.read_sql(query,conn))
 
query = """SELECT Product, TotalPrice
             FROM sales
             ORDER BY TotalPrice ASC;"""
print(pd.read_sql(query,conn))


#GROUP BY Product
query = """SELECT Product,SUM(TotalPrice) AS Revenue
             FROM sales
             GROUP BY Product
             ORDER BY Revenue DESC;"""
print(pd.read_sql(query,conn))

#Average Revenue per product
query = """SELECT Product,AVG(TotalPrice) AS Average_Revenue
             FROM sales
             GROUP BY Product
             ORDER BY Average_Revenue DESC;"""
print(pd.read_sql(query,conn))

#count ORDER BY Product
query = """SELECT Product,COUNT(*) AS Total_Orders
             FROM sales
             GROUP BY Product ;"""
print(pd.read_sql(query,conn))

#Analyse PaymentMethods
query = """SELECT PaymentMethod,COUNT(*) AS Total_Transactions
             FROM sales
             GROUP BY PaymentMethod
             ORDER BY  Total_Transactions DESC;"""
print(pd.read_sql(query,conn))

#analyse Order STatus
query = """SELECT OrderStatus,COUNT(*) AS Orders
             FROM sales
             GROUP BY OrderStatus
             ORDER BY  Orders DESC;"""
print(pd.read_sql(query,conn))

#analyse Top 20 customers
query = """SELECT CustomerID,SUM(TotalPrice) AS Revenue
             FROM sales
             GROUP BY CustomerID
             ORDER BY  Revenue DESC
             LIMIT 20;"""
print(pd.read_sql(query,conn))

# Monthly Revenue
query = """SELECT strftime('%m',Date) as Month,
             SUM (TotalPrice) AS Revenue
             FROM sales
             GROUP BY Month
             ORDER BY Month;"""
print(pd.read_sql(query,conn))

# Having Revenue Greather then 100000
query = """SELECT Product,SUM(TotalPrice) AS Revenue
             FROM sales
             GROUP BY Product
             HAVING Revenue > 100000;"""
print(pd.read_sql(query,conn))



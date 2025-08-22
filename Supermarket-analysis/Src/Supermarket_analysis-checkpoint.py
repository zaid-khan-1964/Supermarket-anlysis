import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data load
df = pd.read_csv("supermarket_sales.csv")

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns)

# 2. Data cleaning
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df.info())

# 3. EDA
print(df.describe())
print(df.groupby('city')['total'].sum())
print(df['payment'].value_counts())
print(df.groupby('branch')['rating'].mean())

# 4. Graphs
sns.countplot(x='payment', data=df)
plt.title("Payment Method Distribution")
plt.show()

city_sales = df.groupby('city')['total'].sum().reset_index()
sns.barplot(x='city', y='total', data=city_sales)
plt.title("Total Sales by City")
plt.show()

branch_rating = df.groupby('branch')['rating'].mean().reset_index()
sns.barplot(x='branch', y='rating', data=branch_rating)
plt.title("Average Rating by Branch")
plt.show()

product_sales = df.groupby('product_line')['total'].sum().reset_index()
sns.barplot(x='total', y='product_line', data=product_sales)
plt.title("Total Sales by Product Line")
plt.show()

gender_spending = df.groupby('gender')['total'].mean().reset_index()
sns.barplot(x='gender', y='total', data=gender_spending)
plt.title("Average Spending by Gender")
plt.show()

df['day'] = df['date'].dt.day_name()
df['is_weekend'] = df['day'].isin(['Saturday', 'Sunday'])
weekend_sales = df.groupby('is_weekend')['total'].sum().reset_index()
sns.barplot(x='is_weekend', y='total', data=weekend_sales)
plt.title("Weekend vs Weekday Sales")
plt.show()

branch_profit = df.groupby('branch')['gross_income'].sum().reset_index()
sns.barplot(x='branch', y='gross_income', data=branch_profit)
plt.title("Total Profit by Branch")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load karna
df = pd.read_csv("supermarket_sales.csv")

# Duplicate & missing check
print("Duplicate rows:", df.duplicated().sum())
print("Missing values:\n", df.isnull().sum())

# -----------------------
# EDA Plots
# -----------------------

plt.figure(figsize=(12,6))
sns.barplot(x="City", y="Total", data=df, estimator=sum)
plt.title("Total Sales by City")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x="Gender", y="Total", data=df, estimator=sum)
plt.title("Sales by Gender")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="Payment", y="Total", data=df, estimator=sum)
plt.title("Sales by Payment Method")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x="Product line", y="Total", data=df, estimator=sum)
plt.title("Sales by Product Line")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Rating"], bins=10, kde=True)
plt.title("Customer Ratings Distribution")
plt.show()



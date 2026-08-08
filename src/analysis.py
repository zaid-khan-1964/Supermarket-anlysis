import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Data load
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Data", "supermarket_sales.csv")

df = pd.read_csv(DATA_PATH)

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

# Payment Method Distribution
sns.countplot(x='payment', data=df)
plt.title("Payment Method Distribution")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "payment_method_distribution.png")
)
plt.show()


# Total Sales by City
city_sales = df.groupby('city')['total'].sum().reset_index()

sns.barplot(x='city', y='total', data=city_sales)
plt.title("Total Sales by City")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "total_sales_by_city.png")
)
plt.show()


# Average Rating by Branch
branch_rating = df.groupby('branch')['rating'].mean().reset_index()

sns.barplot(x='branch', y='rating', data=branch_rating)
plt.title("Average Rating by Branch")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "average_rating_by_branch.png")
)
plt.show()


# Total Sales by Product Line
product_sales = df.groupby('product_line')['total'].sum().reset_index()

sns.barplot(x='total', y='product_line', data=product_sales)
plt.title("Total Sales by Product Line")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "total_sales_by_product_line.png")
)
plt.show()


# Average Spending by Gender
gender_spending = df.groupby('gender')['total'].mean().reset_index()

sns.barplot(x='gender', y='total', data=gender_spending)
plt.title("Average Spending by Gender")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "average_spending_by_gender.png")
)
plt.show()


# Weekend vs Weekday Sales
df['day'] = df['date'].dt.day_name()
df['is_weekend'] = df['day'].isin(['Saturday', 'Sunday'])

weekend_sales = df.groupby('is_weekend')['total'].sum().reset_index()

sns.barplot(x='is_weekend', y='total', data=weekend_sales)
plt.title("Weekend vs Weekday Sales")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "weekend_vs_weekday_sales.png")
)
plt.show()


# Total Profit by Branch
branch_profit = df.groupby('branch')['gross_income'].sum().reset_index()

sns.barplot(x='branch', y='gross_income', data=branch_profit)
plt.title("Total Profit by Branch")
plt.savefig(
    os.path.join(BASE_DIR, "plots", "total_profit_by_branch.png")
)
plt.show()


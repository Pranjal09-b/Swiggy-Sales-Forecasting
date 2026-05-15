import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

df = pd.read_csv('data/swiggy_sales_data.csv')

print(df.head())
print(df.info())
print(df.describe())

# Total sales trend
plt.figure(figsize=(12,6))
plt.plot(df['sales'])
plt.title('Sales Trend')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.show()

# Orders by city
plt.figure(figsize=(8,5))
sns.barplot(x='city', y='orders', data=df)
plt.title('Orders by City')
plt.show()

# Weather impact
plt.figure(figsize=(8,5))
sns.boxplot(x='weather', y='sales', data=df)
plt.title('Weather vs Sales')
plt.show()
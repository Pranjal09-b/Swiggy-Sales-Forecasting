import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

rows = 1000
start_date = datetime(2025, 1, 1)

cities = ['Pune', 'Mumbai', 'Delhi', 'Bangalore']
weather_conditions = ['Sunny', 'Rainy', 'Cloudy']

records = []

for i in range(rows):
    date = start_date + timedelta(days=i % 365)
    city = np.random.choice(cities)
    weather = np.random.choice(weather_conditions)
    festival = np.random.choice([0, 1], p=[0.9, 0.1])
    orders = np.random.randint(50, 500)
    avg_order_value = np.random.randint(150, 600)

    sales = orders * avg_order_value

    records.append([
        date,
        city,
        weather,
        festival,
        orders,
        avg_order_value,
        sales
    ])

columns = [
    'date',
    'city',
    'weather',
    'festival',
    'orders',
    'avg_order_value',
    'sales'
]


df = pd.DataFrame(records, columns=columns)

df.to_csv('data/swiggy_sales_data.csv', index=False)

print('Dataset generated successfully!')
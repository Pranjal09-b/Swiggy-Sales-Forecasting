import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load('models/sales_model.pkl')
st.title("Swiggy Sales Forecasting Dashboard")

# Inputs
city = st.selectbox('City', ['Pune', 'Mumbai', 'Delhi', 'Bangalore'])

weather = st.selectbox('Weather', ['Sunny', 'Rainy', 'Cloudy'])

festival = st.selectbox('Festival', [0, 1])

orders = st.slider('Orders', 50, 500, 100)

avg_order_value = st.slider('Average Order Value', 100, 1000, 250)

# Encoding
city_mapping = {
    'Bangalore': 0,
    'Delhi': 1,
    'Mumbai': 2,
    'Pune': 3
}

weather_mapping = {
    'Cloudy': 0,
    'Rainy': 1,
    'Sunny': 2
}

city_encoded = city_mapping[city]
weather_encoded = weather_mapping[weather]

# Prediction
input_data = pd.DataFrame({
    'city': [city_encoded],
    'weather': [weather_encoded],
    'festival': [festival],
    'orders': [orders],
    'avg_order_value': [avg_order_value]
})

prediction = model.predict(input_data)[0]

st.success(f'Predicted Sales: ₹ {prediction:,.2f}')

# Graph Section
st.subheader("Sales Trend Graph")

sales_data = [20000, 35000, 30000, 45000, 50000, 60000, 55000]

fig, ax = plt.subplots()

ax.plot(sales_data)

ax.set_xlabel("Days")
ax.set_ylabel("Sales")
ax.set_title("Weekly Sales Trend")

st.pyplot(fig)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset

df = pd.read_csv('data/swiggy_sales_data.csv')

# Encode categorical columns

city_encoder = LabelEncoder()
weather_encoder = LabelEncoder()


df['city'] = city_encoder.fit_transform(df['city'])
df['weather'] = weather_encoder.fit_transform(df['weather'])

# Features and target

X = df[['city', 'weather', 'festival', 'orders', 'avg_order_value']]
y = df['sales']

# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions

predictions = model.predict(X_test)

# Evaluation

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'MAE: {mae}')
print(f'R2 Score: {r2}')

# Save model

joblib.dump(model, 'models/sales_model.pkl')

print('Model trained and saved successfully!')
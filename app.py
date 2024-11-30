import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the trained model and scaler
with open('kmeans_model.pkl', 'rb') as model_file:
    kmeans = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define the feature column names that match the order used during training
FEATURE_COLUMNS = [
    "Order_Quantity", "Unit_Cost", "Unit_Price", "Profit", "Cost", "Revenue"
]

# Define the API route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the frontend
    data = request.get_json()

    # Extract individual fields from the data
    order_quantity = data["Order_Quantity"]
    unit_cost = data["Unit_Cost"]
    unit_price = data["Unit_Price"]
    profit = data["Profit"]
    cost = data["Cost"]
    revenue = data["Revenue"]

    # Prepare the input data for prediction, ensuring column order matches training
    input_data = pd.DataFrame([{
        "Order_Quantity": order_quantity,
        "Unit_Cost": unit_cost,
        "Unit_Price": unit_price,
        "Profit": profit,
        "Revenue": revenue,
        "Cost": cost
    }])

    # Ensure the columns are in the same order as the training data
    input_data = input_data[FEATURE_COLUMNS]

    # Apply scaling using the loaded scaler
    scaled_data = scaler.transform(input_data)

    # Make a prediction using the loaded model
    cluster = kmeans.predict(scaled_data)

    # Return the prediction as a JSON response
    return jsonify({"cluster": int(cluster[0])})

if __name__ == '__main__':
    app.run(debug=True)
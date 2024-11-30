# Project Title: Customer Segmentation Model Deployment
------------------------------------------

## Project Overview

- This project is a machine learning-powered Customer Segmentation Application that uses KMeans clustering to group customers into distinct clusters based on features such as order quantity, unit cost, profit, and revenue. The application is deployed on Render, offering a seamless web-based interface for user interaction and prediction.
- The KMeans clustering model was trained on preprocessed data and deployed using Flask, which serves as the backend API. Flask handles the rendering of the machine learning model, scaler, and front-end page while collecting input from the user through a form. It provides immediate and accurate cluster predictions, enabling users to get feedback quickly and effectively.
---------------------------------------------------

## Project Structure

- Customer_Segmentation/
- │
- ├── templates/
- │   └── index.html               # HTML front-end form to collect user input and call the API
- ├── app.py                       # Flask app for API that serves the model, scaler, and index.html files
- ├── kmeans_model.pkl             # Trained machine learning model (KMeans)
- ├── scaler.pkl                   # Scaler used for data preprocessing
- ├── requirements.txt             # Python dependencies for Flask, scikit-learn, pandas, numpy
- ├── Procfile                     # Configuration for deploying the Flask app on Render
- ├── Customer_Segmentation_Model.ipynb  # Jupyter Notebook for training the KMeans model
- ├── Customer_Segmentation_py.csv # Dataset used in the Jupyter Notebook for training the model
- └── README.md                    # Project documentation
-------------------------------------

## How to setup and run the Application locally

**Installation**
- Clone the github repository https://github.com/Ehnkay-Bassie/Customer_Segmentation.git or download the files in the repository and save in the structure above.
- Install dependencies:
```
  pip install -r requirements.txt.
```
- Run the 'Customer_Segmentation_Model.ipynb' python notebook to create and save the 'kmeans_model.pkl'and the 'scaler.pkl' files.
- Ensure the dataset 'Customer_Segmentation_py.csv' is in the same directory as the python notebook.
- Run the app.py file to render the saved model and scaler, and the index.html frontend form.

**Web Interface Usage**
- You can also open your browser and navigate to http://127.0.0.1:5000 to access the html form while the app.py file is running.
- Select or input values for the Product Category and Order Quantity fields
- The Unit Price for each product is displayed in the dropdown menu based on the selected product category. The Unit Cost is pre-determined based on the selected product category.
- The Profit, Cost, and Revenue values are automatically calculated based on the provided Order Quantity, Unit Price, and Unit Cost of the selected product.
- Once the necessary inputs are provided, click the Submit button to get the cluster prediction. The model will use the input data to determine which cluster the customer belongs to based on the trained KMeans model.
------------------------------  

## Steps for Live Deployment

1. **Set Up Render Account:**
   - Create an account on Render (if not already done) and log into the dashboard.

2. **Create a New Web Service on Render:**
   - A new Python web service was created on Render.
   - The GitHub repository containing the project files (including the Flask app, model files, and front-end HTML) was linked to the service on Render.

3. **Configuration for Deployment:**
   - **Procfile**: A `Procfile` was added to the project, specifying the command needed to run the Flask app. This file tells Render to run the app with the command:
     ```
     web: python app.py
     ```
   - **requirements.txt**: The `requirements.txt` file includes all the necessary dependencies for the project, such as Flask, scikit-learn, pandas, and numpy, which are essential for both the web framework and machine learning functionalities.
   - **Environment Variables**: There were no additional environment variables required for this project, but this step would be essential if the application required external keys or sensitive data.

4. **Build and Deploy:**
   - After linking the GitHub repository and configuring all necessary files, the deployment process was triggered. Render automatically installed the dependencies from `requirements.txt`, built the app, and launched it in the cloud.
   - The application was then tested to ensure it was accessible and functioning as expected, with the front-end form able to submit input data, and the API returning correct cluster predictions.

5. **Accessing the Application:**
   - Once deployed, Render provided a unique URL for the application: https://customer-segmentation-6pc2.onrender.com/ 
   - The web interface at this URL enables users to enter details like Order Quantity and Product Category, and receive instant predictions of customer segments (clusters) based on the input data.

## Monitoring and Maintenance

- The Render dashboard offers real-time monitoring for the deployed service, providing access to logs and error tracking, which helps ensure that the application runs smoothly.
- For any updates to the project, such as bug fixes or model retraining, the changes are pushed to the GitHub repository. Render automatically detects these updates and redeploys the application with the latest changes.

** The live application can be accessed here: https://customer-segmentation-6pc2.onrender.com/ **
------------------------------------------------

## Technologies Used

- **Python**: Backend logic and API development.
- **Flask**: Web framework for serving the application.
- **scikit-learn**: Machine learning library used for training the KMeans model.
- **pandas & numpy**: Data manipulation and preprocessing.
- **Render**: Cloud platform for deploying the Flask application.
-------------------------------------------------

*Author: Nnanke Bassey*

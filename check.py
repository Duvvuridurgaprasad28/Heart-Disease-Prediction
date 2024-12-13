from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle 

app = Flask(__name__)

model = pickle.load(open("heart_disease_model.pkl","rb"))

# Sample data for testing
test_data = np.array([[55,1,0,132,353,0,1,132,1,1.2,1,1,3]])
print(model.predict(test_data))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve and convert form data
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Prepare data for prediction
        data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Debug: Print the data
        print("Data for prediction:", data)

        # Perform prediction
        prediction = model.predict(data)

        # Debug: Print the prediction
        print("Prediction:", prediction)

        # Create result message based on prediction
        result_message = "The person has Heart Disease based on the provided data." if prediction[0] == 1 else "The person does not have heart disease based on the provided data."

    except Exception as e:
        # Handle errors
        result_message = f"An error occurred: {e}"

    # Render the template with the result message
    return render_template("predict.html", message=result_message)

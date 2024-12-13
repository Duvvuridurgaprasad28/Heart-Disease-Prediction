from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

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
        print(f"Data for prediction: {data}")

        # Perform prediction
        prediction = model.predict(data)

        # Debug: Print the prediction
        print(f"Prediction: {prediction}")

        # Create result message based on prediction
        result_message = "The person has Heart Disease based on the provided data." if prediction[0] == 1 else "The person does not have heart disease based on the provided data."

    except Exception as e:
        # Handle errors
        result_message = f"An error occurred: {e}"

    # Render the template with the result message
    return render_template("predict.html", message=result_message)

if __name__ == '__main__':
    app.run(debug=True)

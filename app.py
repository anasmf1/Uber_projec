from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)
# Charger le modèle et le scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = joblib.load(scaler_file)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction')
def predict_page():
    return render_template('prediction.html')
# Route pour effectuer la prédiction
@app.route('/predict', methods=['POST'])
def predict():
       # Récupération des données du formulaire
    passenger_count = int(request.json['passenger_count'])
    year = int(request.json['year'])
    month = int(request.json['month'])
    day = int(request.json['day'])
    hour = int(request.json['hour'])
    distance = float(request.json['distance'])

    # Mise en forme des données d'entrée
    input_data = np.array([[passenger_count, year, month, day, hour, distance]])
    input_data_scaled = scaler.transform(input_data)

    # Prédiction
    prediction = model.predict(input_data_scaled)
    fare = round(prediction[0], 2)

    return jsonify({'prediction': fare})

@app.route('/status')
def status_page():
    return render_template('status.html')
@app.route('/status', methods=['POST'])  # Changer GET à POST
def tester():
    return jsonify({'status': ' All systems are operational. '})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
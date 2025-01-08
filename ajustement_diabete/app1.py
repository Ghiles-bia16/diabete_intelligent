import pandas as pd
from flask import Flask, request, render_template, jsonify
import joblib
import torch
from NLP.chat import get_response as get_response_fr
from NLP.chatang import get_response as get_response_en


model_xgb = joblib.load('xgb_model.pkl') 
model2=joblib.load('model2.pkl')

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('Acceuil.html')



@app.route('/FAQ', methods=['GET', 'POST'])
def FAQ():
    if request.method == 'GET':
        return render_template('FAQ.html')
    else:  # POST request
        data = request.get_json()
        text = data.get('message')
        response = get_response_fr(text)  # Use French response
        return jsonify({'response': response})
    
@app.route('/simulateur', methods=['GET', 'POST'])  
def simulateur():
    prediction = None
    prediction_simple = None
    
    if request.method == 'POST':
       
        if 'HbA1c_level' in request.form and 'blood_glucose_level' in request.form:
            age = int(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            bmi = float(request.form['bmi'])
            HbA1c_level = float(request.form['HbA1c_level'])
            blood_glucose_level = float(request.form['blood_glucose_level'])
            gender = request.form['gender']
            smoking_history = request.form['smoking_history']

            gender_encoded = {'gender_Female': 0, 'gender_Male': 0}
            gender_encoded[f'gender_{gender}'] = 1
            
            smoking_history_encoded = {
                'smoking_history_No Info': 0, 
                'smoking_history_current': 0, 
                'smoking_history_ever': 0,
                'smoking_history_former': 0,
                'smoking_history_never': 0,
                'smoking_history_not current': 0
            }
            smoking_history_encoded[f'smoking_history_{smoking_history}'] = 1
            
            input_data = pd.DataFrame({
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'bmi': [bmi],
                'HbA1c_level': [HbA1c_level],
                'blood_glucose_level': [blood_glucose_level],
                **gender_encoded,
                **smoking_history_encoded
            })
            
            prediction = model_xgb.predict(input_data)[0]
  
        if 'HbA1c_level' not in request.form or 'blood_glucose_level' not in request.form:
            age = int(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            bmi = float(request.form['bmi'])
            gender = request.form['gender']
            smoking_history = request.form['smoking_history']
            
            gender_encoded = {'gender_Female': 0, 'gender_Male': 0}
            gender_encoded[f'gender_{gender}'] = 1
            
            smoking_history_encoded = {
                'smoking_history_No Info': 0, 
                'smoking_history_current': 0, 
                'smoking_history_ever': 0,
                'smoking_history_former': 0,
                'smoking_history_never': 0,
                'smoking_history_not current': 0
            }
            smoking_history_encoded[f'smoking_history_{smoking_history}'] = 1
            
            input_data = pd.DataFrame({
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'bmi': [bmi],
                **gender_encoded,
                **smoking_history_encoded
            })
            
            prediction_simple = model2.predict(input_data)[0]
        
    return render_template('simulateur.html', prediction=prediction, prediction_simple=prediction_simple)

@app.route('/contacts')
def contacts():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/benefit', methods=['GET', 'POST'])
def benefit():
    prediction = None
    prediction_simple = None
    
    if request.method == 'POST':
        if 'HbA1c_level' in request.form and 'blood_glucose_level' in request.form:
            age = int(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            bmi = float(request.form['bmi'])
            HbA1c_level = float(request.form['HbA1c_level'])
            blood_glucose_level = float(request.form['blood_glucose_level'])
            gender = request.form['gender']
            smoking_history = request.form['smoking_history']

            gender_encoded = {'gender_Female': 0, 'gender_Male': 0}
            gender_encoded[f'gender_{gender}'] = 1
            
            smoking_history_encoded = {
                'smoking_history_No Info': 0, 
                'smoking_history_current': 0, 
                'smoking_history_ever': 0,
                'smoking_history_former': 0,
                'smoking_history_never': 0,
                'smoking_history_not current': 0
            }
            smoking_history_encoded[f'smoking_history_{smoking_history}'] = 1
            
            input_data = pd.DataFrame({
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'bmi': [bmi],
                'HbA1c_level': [HbA1c_level],
                'blood_glucose_level': [blood_glucose_level],
                **gender_encoded,
                **smoking_history_encoded
            })
            
            prediction = model_xgb.predict(input_data)[0]
  
        if 'HbA1c_level' not in request.form or 'blood_glucose_level' not in request.form:
            age = int(request.form['age'])
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            bmi = float(request.form['bmi'])
            gender = request.form['gender']
            smoking_history = request.form['smoking_history']
            
            gender_encoded = {'gender_Female': 0, 'gender_Male': 0}
            gender_encoded[f'gender_{gender}'] = 1
            
            smoking_history_encoded = {
                'smoking_history_No Info': 0, 
                'smoking_history_current': 0, 
                'smoking_history_ever': 0,
                'smoking_history_former': 0,
                'smoking_history_never': 0,
                'smoking_history_not current': 0
            }
            smoking_history_encoded[f'smoking_history_{smoking_history}'] = 1
            
            input_data = pd.DataFrame({
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [heart_disease],
                'bmi': [bmi],
                **gender_encoded,
                **smoking_history_encoded
            })
            prediction_simple = model2.predict(input_data)[0]
    return render_template('benefit.html', prediction=prediction, prediction_simple=prediction_simple)
@app.route('/faq-en', methods=['GET', 'POST'])
def FAQ_EN():
    if request.method == 'GET':
        return render_template('FAQ_en.html')
    else:  # POST request
        data = request.get_json()
        text = data.get('message')
        response = get_response_en(text)  # Use English response
        return jsonify({'response': response})

@app.route('/contact-en')
def contact_en():
    return render_template('contact_en.html')


if __name__ == '__main__':
    app.run(debug=True)

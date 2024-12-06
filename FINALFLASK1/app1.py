import pandas as pd
from flask import Flask, request, render_template
import joblib


model = joblib.load('xgb_model.pkl')  

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('Acceuil.html')

@app.route('/simulateur', methods=['GET', 'POST'], endpoint='simulateur')
def predict():
    prediction = None
    
    if request.method == 'POST':
         
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
            
            
            prediction = model.predict(input_data)[0]
    
    
    
    return render_template('simulateur.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


model = joblib.load('model1&&.pkl')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
       
        age = float(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        bmi = float(request.form['bmi'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = float(request.form['blood_glucose_level'])  
        gender = request.form['gender']
        smoking_history = request.form['smoking_history']
        
        gender_encoded = {'gender_Female': 0, 'gender_Male': 0}
        gender_encoded[f'gender_{gender}'] = 1
        
        smoking_history_encoded = {'smoking_history_No Info': 0, 'smoking_history_current': 0, 'smoking_history_ever': 0 ,'smoking_history_former': 0 ,'smoking_history_never': 0 ,'smoking_history_not current': 0 }
        smoking_history_encoded[f'smoking_history_{smoking_history}'] = 1
        
        

        scaler = MinMaxScaler()
        numerical_features = scaler.fit_transform([[age, hypertension, heart_disease, bmi,
                                                    HbA1c_level,blood_glucose_level]])[0]
        
        input_data =  pd.DataFrame({
            'age': [numerical_features[0]],
            'hypertension': [numerical_features[1]],
            'heart_disease': [numerical_features[2]],
            'bmi': [numerical_features[3]],
            'HbA1c_level': [numerical_features[4]],
            'blood_glucose_level': [numerical_features[5]],
            **gender_encoded,
            **smoking_history_encoded,
        })
        
        
        prediction = model.predict(input_data)[0]
        
      
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




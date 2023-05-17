import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'gender': 'Male','age': '42','hypertension': 'No','heart_disease': 'No',
                            'ever_married': 'Yes','work_type': 'Private',
                            'Residence_type': 'Rural','avg_glucose_level': '83.41',
                            'bmi': '25.4','smoking_status': 'Unknown'})

print(r.json())


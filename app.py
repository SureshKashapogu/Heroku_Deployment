# code copied from
# https://github.com/krishnaik06/Heroku-Demo/blob/master/app.py



import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    output = None
    '''
    For rendering results on HTML GUI
    '''
    features = [int(float(x)) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    
    if prediction == 0:
        output = "Not at risk for stroke"
    if prediction == 1:
        output = "At risk for stroke"

    return render_template('index.html', prediction_text='Predicted Stroke Status: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
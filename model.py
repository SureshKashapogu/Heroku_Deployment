import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('healthcare-dataset-stroke-data.csv')

dataset['bmi'].fillna(dataset['bmi'].mean(), inplace=True)

def convert_to_int_for_gender(gender):
    word_dict = {'Male':1, 'Female':0, 'Other':3}
    return word_dict[gender]

dataset['gender'] = dataset['gender'].apply(lambda x : convert_to_int_for_gender(x))

def convert_to_int_for_ever_married(ever_married):
    word_dict = {'No':0, 'Yes':1}
    return word_dict[ever_married]

dataset['ever_married'] = dataset['ever_married'].apply(lambda x : convert_to_int_for_ever_married(x))

def convert_to_int_for_work_type(work_type):
    word_dict = {'Self-employed':0, 'Private':1, 'Govt_job':2, 'children':3, 'Never_worked':4}
    return word_dict[work_type]

dataset['work_type'] = dataset['work_type'].apply(lambda x : convert_to_int_for_work_type(x))

def convert_to_int_for_Residence_type(Residence_type):
    word_dict = {'Rural':0, 'Urban':1}
    return word_dict[Residence_type]

dataset['Residence_type'] = dataset['Residence_type'].apply(lambda x : convert_to_int_for_Residence_type(x))

def convert_to_int_for_smoking_status(smoking_status):
    word_dict = {'never smoked':0, 'formerly smoked':1, 'smokes':2, 'Unknown':3}
    return word_dict[smoking_status]

dataset['smoking_status'] = dataset['smoking_status'].apply(lambda x : convert_to_int_for_smoking_status(x))



X = dataset.iloc[:, 1:11]
y = dataset.iloc[:, -1]


from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()

classifier.fit(X,y)

pickle.dump(classifier, open('model.pkl','wb'))



model = pickle.load(open('model.pkl','rb'))
check = [1,42,0,0,1,1,0,83.41,25.4,3]
int_features = [int(float(x)) for x in check]
final_features = [np.array(int_features)]
prediction = model.predict(final_features)


if prediction == 0:
    print("Not at risk for stroke")
if prediction == 1:
    print("At risk for stroke")







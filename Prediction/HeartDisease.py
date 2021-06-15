import pickle
import pandas as pd

file = "Models/HeartModel.sav"
load_model = pickle.load(open(file, 'rb'))


def heartpredict(age, gender, chestPain, trestbps, chol, fbs, restecg, thalach, exang, oldpeaks, slope, ca, thal):
    user_input = pd.DataFrame(
        {'Age': [age], 'sex': [gender], 'cp': [chestPain], 'trestbps': [trestbps], 'chol': [chol], 'fbs': [fbs],
         'restecg': [restecg], 'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeaks], 'slope': [slope],
         'ca': [ca], 'thal': [thal]})

    prediction = load_model.predict(user_input)
    if prediction == 1.:
        return "Heart Disease"
    else:
        return "No Heart Disease"

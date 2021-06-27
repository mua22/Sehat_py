import pickle
import pandas as pd


def HVJFp(temperature, pulse_rate, la_pain, ua_pain, vomiting_feeling, yellowish_urine, indigestion):
    filename = 'Models/fourdiseases.sav'
    load_model = pickle.load(open(filename, 'rb'))

    user_input = pd.DataFrame(
        {'Temperature': [temperature], 'Pulse_Rate': [pulse_rate], 'LA_Pain': [la_pain], 'UA_Pain': [ua_pain],
         'Vomiting_Feeling': [vomiting_feeling], 'Yellowish_Urine': [yellowish_urine], 'Indigestion': [indigestion]})
    predictions = load_model.predict(user_input)
    if predictions == 0:
        return "Heart Disease"
    if predictions == 1:
        return "Viral Fever or Cold"
    if predictions == 2:
        return "Jaundice"
    if predictions == 3:
        return "Food Poisoning"
    if predictions == 4:
        return "Normal"

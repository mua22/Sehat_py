import pickle
import pandas as pd

file = "Models/SymptomBestmodel.pkl"
load_model = pickle.load(open(file, 'rb'))


def SymptomPrediction(itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, chills, joint_pain,
            muscle_wasting, vomiting, fatigue, weight_loss, restlessness, irregular_sugar_level, cough, high_fever,
            breathlessness, sweating, headache):

    user_input = pd.DataFrame(
        {'itching': [itching], 'skin_rash': [skin_rash], 'nodal_skin_eruptions': [nodal_skin_eruptions],
         'continuous_sneezing': [continuous_sneezing],
         'shivering': [shivering], 'chills': [chills], 'joint_pain': [joint_pain], 'muscle_wasting': [muscle_wasting],
         'vomiting': [vomiting], 'fatigue': [fatigue], 'weight_loss': [weight_loss], 'restlessness': [restlessness],
         'lethargy': [0], 'patches_in_throat': [0], 'irregular_sugar_level': [irregular_sugar_level], 'cough': [cough],
         'high_fever': [high_fever], 'breathlessness': [breathlessness], 'sweating': [sweating], 'headache': [headache],
         'yellowish_skin': [0],  'dark_urine': [0], 'nausea': [0], 'loss_of_appetite': [0], 'pain_behind_the_eyes': [0], 'back_pain': [0],
         'abdominal_pain': [0], 'diarrhoea': [0], 'mild_fever': [0], 'yellow_urine': [0], 'yellowing_of_eyes': [0],
         'acute_liver_failure': [0], 'swelled_lymph_nodes': [0], 'malaise': [0], 'blurred_and_distorted_vision': [0],
         'phlegm': [0], 'throat_irritation': [0], 'redness_of_eyes': [0], 'sinus_pressure': [0], 'runny_nose': [0],
         'congestion': [0], 'chest_pain': [0], 'fast_heart_rate': [0], 'obesity': [0], 'excessive_hunger': [0],
         'extra_marital_contacts': [0], 'loss_of_smell': [0], 'muscle_pain': [0], 'red_spots_over_body': [0],
         'dischromic _patches': [0], 'watering_from_eyes': [0], 'increased_appetite': [0], 'polyuria': [0],
         'family_history': [0], 'rusty_sputum': [0], 'receiving_blood_transfusion': [0],
         'receiving_unsterile_injections': [0],
         'coma': [0], 'stomach_bleeding': [0]})

    print('helllp')
    prediction = load_model.predict(user_input)
    print(prediction[0])
    return prediction[0]

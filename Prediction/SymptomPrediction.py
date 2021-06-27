import pickle
import pandas as pd

file = "Models/SymptomBestmodel.pkl"
load_model = pickle.load(open(file, 'rb'))


def SymptomPrediction(itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, chills, joint_pain,
            muscle_wasting, vomiting, fatigue, weight_loss, restlessness, lethargy, patches_in_throat, irregular_sugar_level, cough, high_fever,
            breathlessness, sweating, headache, yellowish_skin, dark_urine, nausea, loss_of_appetite, pain_behind_the_eyes,
            back_pain , abdominal_pain, diarrhoea , mild_fever, yellow_urine, yellowing_of_eyes, acute_liver_failure,
            swelled_lymph_nodes, malaise, blurred_and_distorted_vision, phlegm, throat_irritation, redness_of_eyes,
            sinus_pressure, runny_nose, congestion, chest_pain, fast_heart_rate, obesity, excessive_hunger, extra_marital_contacts,
            loss_of_smell, muscle_pain, red_spots_over_body, dischromic_patches, watering_from_eyes, increased_appetite, polyuria,
            rusty_sputum, receiving_blood_transfusion, receiving_unsterile_injections, stomach_bleeding):

    user_input = pd.DataFrame(
        {'itching': [itching], 'skin_rash': [skin_rash], 'nodal_skin_eruptions': [nodal_skin_eruptions],
         'continuous_sneezing': [continuous_sneezing],
         'shivering': [shivering], 'chills': [chills], 'joint_pain': [joint_pain], 'muscle_wasting': [muscle_wasting],
         'vomiting': [vomiting], 'fatigue': [fatigue], 'weight_loss': [weight_loss], 'restlessness': [restlessness],
         'lethargy': [lethargy], 'patches_in_throat': [patches_in_throat], 'irregular_sugar_level': [irregular_sugar_level], 'cough': [cough],
         'high_fever': [high_fever], 'breathlessness': [breathlessness], 'sweating': [sweating], 'headache': [headache],
         'yellowish_skin': [yellowish_skin],  'dark_urine': [dark_urine], 'nausea': [nausea], 'loss_of_appetite': [loss_of_appetite],
         'pain_behind_the_eyes': [pain_behind_the_eyes], 'back_pain': [back_pain],
         'abdominal_pain': [abdominal_pain], 'diarrhoea': [diarrhoea], 'mild_fever': [mild_fever], 'yellow_urine': [yellow_urine], 'yellowing_of_eyes': [yellowing_of_eyes],
         'acute_liver_failure': [acute_liver_failure], 'swelled_lymph_nodes': [swelled_lymph_nodes], 'malaise': [malaise], 'blurred_and_distorted_vision': [blurred_and_distorted_vision],
         'phlegm': [phlegm], 'throat_irritation': [throat_irritation], 'redness_of_eyes': [redness_of_eyes], 'sinus_pressure': [sinus_pressure], 'runny_nose': [runny_nose],
         'congestion': [congestion], 'chest_pain': [chest_pain], 'fast_heart_rate': [fast_heart_rate], 'obesity': [obesity], 'excessive_hunger': [excessive_hunger],
         'extra_marital_contacts': [extra_marital_contacts], 'loss_of_smell': [loss_of_smell], 'muscle_pain': [muscle_pain], 'red_spots_over_body': [red_spots_over_body],
         'dischromic_patches': [dischromic_patches], 'watering_from_eyes': [watering_from_eyes], 'increased_appetite': [increased_appetite], 'polyuria': [polyuria],
         'family_history': [0], 'rusty_sputum': [rusty_sputum], 'receiving_blood_transfusion': [receiving_blood_transfusion],
         'receiving_unsterile_injections': [receiving_unsterile_injections],
         'coma': [0], 'stomach_bleeding': [stomach_bleeding]})

    print('helllp')
    prediction = load_model.predict(user_input)
    print(prediction[0])
    return prediction[0]

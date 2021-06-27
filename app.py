from flask import Flask, render_template, request
import datetime

from ImageEnhancement.imgE import ImageEnhacement
from Prediction.H_Vf_J_Fp_Disease import HVJFp
from Prediction.HeartDisease import heartpredict
from Prediction.SymptomPrediction import SymptomPrediction

app = Flask(__name__)

prediction = ""


@app.route('/', methods=['GET'])
def HelloWorld():
    return "Hello Form AI"


@app.route('/api/ai/heart_disease', methods=['GET', 'POST'])
def heart():
    print("Heart")
    if request.method == 'POST':
        content = request.json
        try:
            print("Get the Post request")

            print(request.json)
            age = content['age']
            gender = content['sex']
            chestPain = content['chestPain']
            trestbps = content['trestbps']
            chol = content['chol']
            fbs = content['fbs']
            restecg = content['restecg']
            thalach = content['thalach']
            exang = content['exang']
            oldpeaks = content['oldpeak']
            slope = content['slope']
            ca = content['ca']
            thal = content['thal']
            print("hello")

            return heartpredict(age, gender, chestPain, trestbps, chol, fbs, restecg, thalach, exang,
                                oldpeaks, slope, ca, thal)

        except Exception as e:
            return e


@app.route('/api/ai/HVJFp', methods=['GET', 'POST'])
def HVJFP():
    if request.method == 'POST':
        content = request.json
        try:
            print(content)
            temperature = content['temperature']
            pulse_rate = content['pulse_rate']
            la_pain = content['la_pain']
            ua_pain = content['ua_pain']
            vomiting_feeling = content['vomiting_feeling']
            yellowish_urine = content['yellowish_urine']
            indigestion = content['indigestion']
            return HVJFp(temperature, pulse_rate, la_pain, ua_pain, vomiting_feeling, yellowish_urine, indigestion)
        except Exception as e:
            return e
    else:
        return "0"


@app.route('/api/ai/image_enhacement', methods=['GET', 'POST'])
def IE():
    if request.method == 'POST':
        content = request.json
        try:
            bas64_image = content['pic_base64']
            return ImageEnhacement(bas64_image)
        except Exception as e:
            return e
    else:
        return "Error in Image Enhacement"


@app.route('/api/ai/symptonpredicton', methods=['GET', 'POST'])
def symmp():
    if request.method == 'POST':
        content = request.json
        # try:
        itching = content['itching']
        skin_rash = content['skin_rash']
        nodal_skin_eruptions = content['nodal_skin_eruptions']
        continuous_sneezing = content['continuous_sneezing']
        shivering = content['shivering']
        chills = content['chills']
        joint_pain = content['joint_pain']
        muscle_wasting = content['muscle_wasting']
        vomiting = content['vomiting']
        fatigue = content['fatigue']
        weight_loss = content['weight_loss']
        restlessness = content['restlessness']
        irregular_sugar_level = content['irregular_sugar_level']
        cough = content['cough']
        high_fever = content['high_fever']
        breathlessness = content['breathlessness']
        lethargy = content['lethargy']
        patches_in_throat = content['patches_in_throat']
        sweating = content['sweating']
        yellowish_skin = content['yellowish_skin']
        dark_urine = content['dark_urine']
        nausea = content['nausea']
        loss_of_appetite = content['loss_of_appetite']
        pain_behind_the_eyes = content['pain_behind_the_eyes']
        back_pain = content['back_pain']
        abdominal_pain = content['abdominal_pain']
        diarrhoea = content['diarrhoea']
        mild_fever = content['mild_fever']
        yellow_urine = content['yellow_urine']
        headache = content['headache']
        acute_liver_failure = content['acute_liver_failure']
        swelled_lymph_nodes = content['swelled_lymph_nodes']
        malaise = content['malaise']
        blurred_and_distorted_vision = content['blurred_and_distorted_vision']
        phlegm = content['phlegm']
        throat_irritation = content['throat_irritation']
        redness_of_eyes = content['redness_of_eyes']
        sinus_pressure = content['sinus_pressure']
        runny_nose = content['runny_nose']
        congestion = content['congestion']
        chest_pain = content['chest_pain']
        fast_heart_rate = content['fast_heart_rate']
        obesity = content['obesity']
        excessive_hunger = content['excessive_hunger']
        extra_marital_contacts = content['extra_marital_contacts']
        loss_of_smell = content['loss_of_smell']
        muscle_pain = content['muscle_pain']
        red_spots_over_body = content['red_spots_over_body']
        yellowing_of_eyes = content['yellowing_of_eyes']
        increased_appetite = content['increased_appetite']
        polyuria = content['polyuria']
        watering_from_eyes = content['watering_from_eyes']
        receiving_blood_transfusion = content['receiving_blood_transfusion']
        receiving_unsterile_injections = content['receiving_unsterile_injections']
        rusty_sputum = content['rusty_sputum']
        stomach_bleeding = content['stomach_bleeding']
        dischromic_patches = content['dischromic_patches']

        return SymptomPrediction(itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, chills,
                                 joint_pain,
                                 muscle_wasting, vomiting, fatigue, weight_loss, restlessness, lethargy,
                                 patches_in_throat, irregular_sugar_level, cough, high_fever,
                                 breathlessness, sweating, headache, yellowish_skin, dark_urine, nausea,
                                 loss_of_appetite, pain_behind_the_eyes,
                                 back_pain, abdominal_pain, diarrhoea, mild_fever, yellow_urine, yellowing_of_eyes,
                                 acute_liver_failure,
                                 swelled_lymph_nodes, malaise, blurred_and_distorted_vision, phlegm, throat_irritation,
                                 redness_of_eyes,
                                 sinus_pressure, runny_nose, congestion, chest_pain, fast_heart_rate, obesity,
                                 excessive_hunger, extra_marital_contacts,
                                 loss_of_smell, muscle_pain, red_spots_over_body, dischromic_patches,
                                 watering_from_eyes, increased_appetite, polyuria,
                                 rusty_sputum, receiving_blood_transfusion, receiving_unsterile_injections,
                                 stomach_bleeding)
        # except Exception as e:
        #     return e
    else:
        return "0"


if __name__ == '__main__':
    app.run(debug=True)
# host="192.168.0.102"

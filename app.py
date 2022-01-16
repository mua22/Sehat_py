from flask import Flask, request
from flask_cors import CORS, cross_origin
from ImageEnhancement.imgE import ImageEnhacement
from ImageRegistration.fourPointTransform import ImageRegistration
from Prediction.H_Vf_J_Fp_Disease import HVJFp
from Prediction.HeartDisease import heartpredict
from Prediction.SymptomPrediction import SymptomPrediction

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
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


@app.route('/api/ai/imageEnhancement', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
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


@app.route('/api/ai/imageRegistration', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def IR():
    print("hello everyone")
    if request.method == 'POST':
        content = request.json
        try:
            print("hello everyone")
            bas64_image = content['pic_base64']
            return ImageRegistration(bas64_image)
        except Exception as e:
            return e
    else:
        return "Error in Image Enhacement"


@app.route('/api/ai/symptonpredicton', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
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


@app.route('/api/ai/graphs', methods=['GET', 'POST'])
def graph():
    if request.method == 'GET':

        try:
            data = {
                "results": [
                    {
                        "data": {
                            "values": [4000, 3643, 6189, 7122, 7886, 8512, 8214, 8812, 7546, 6879, 6504, 6754],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "5-Jul", "7-Jun",
                                      "14-Jun", "21-Jun", "28-Jun""12-Jul"],
                            "city": "Karachi"
                        }
                    },
                    {
                        "data": {
                            "values": [
                                3454, 3645, 6189, 6189, 7886, 8001, 6500, 5987, 6789, 7812, 7819, 8255
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Sialkot"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                2458,
                                1297,
                                3643,
                                1354,
                                3643,
                                4529,
                                6145,
                                7548,
                                5466,
                                6189,
                                5999,
                                6353,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Faisalabad"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                5000,
                                5700,
                                6189,
                                6189,
                                7886,
                                8214,
                                8812,
                                8000,
                                6478,
                                4500,
                                4505,
                                4456,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Rawalpindi"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                2465,
                                3400,
                                4000,
                                4500,
                                3800,
                                3200,
                                3600,
                                4897,
                                4100,
                                5454,
                                4999,
                                5252,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Peshawar"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                5542,
                                4000,
                                3800,
                                3100,
                                2687,
                                2451,
                                1987,
                                1546,
                                1244,
                                1000,
                                850,
                                381,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Multan"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                1500,
                                2200,
                                2400,
                                2915,
                                3451,
                                3856,
                                4215,
                                4965,
                                5479,
                                6154,
                                6648,
                                7162,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Gujranwala"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                8645,
                                7886,
                                9159,
                                5645,
                                3359,
                                1297,
                                3643,
                                1297,
                                3643,
                                3502,
                                3000,
                                2436,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Lahore"
                        }

                    },
                    {
                        "data": {
                            "values": [
                                0,
                                20,
                                0,
                                156,
                                100,
                                50,
                                110,
                                56,
                                10,
                                65,
                                60,
                                61,
                            ],
                            "dates": ["26-Apr", "3-May", "10-May", "17-May", "24-May", "31-May", "7-Jun", "14-Jun",
                                      "21-Jun", "28-Jun", "5-Jul", "12-Jul"
                                      ],
                            "city": "Gilgit"
                        }

                    },

                ]
            }
            return data
        except Exception as e:
            return e
    else:
        return "Error in Image Enhacement"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#

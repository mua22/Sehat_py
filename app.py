from flask import Flask, render_template, request
import datetime

from ImageEnhancement.imgE import ImageEnhacement
from Prediction.H_Vf_J_Fp_Disease import HVJFp
from Prediction.HeartDisease import heartpredict

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


if __name__ == '__main__':
    app.run(debug=True,host="192.168.0.102")

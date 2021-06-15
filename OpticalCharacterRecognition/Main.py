import pytesseract as pt
import re
import cv2
import json

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filename = "report3.jpg"
image = cv2.imread(filename)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Blur and perform text extraction
thresh = cv2.GaussianBlur(thresh, (3, 3), 0)
text = pt.image_to_string(image, lang='eng')

defined_dict = {'Hospital Name': ['Hospital Name', 'Hospital_Name',
                                  'hospital name'],
                'Hospital Address': ['Address', 'city', 'Hospital Address'],
                'Patient Name': ['Name', 'Patient_Name', 'Patient Name', 'patient name'],
                'Address': ['Patient Address', 'Address', 'Add'],
                'Age': ['Age', 'age'],
                'Sex': ['Sex', 'sex', 'gender', 'Gender', 'M/F', 'Male/Feamal'],
                'Doctor Name': ['Doctor Name', 'doctor name', 'doctor', 'treating doctor',
                                'Consultants', 'CONSULTANT', 'Consultant Name', 'Dr.', 'ref', 'ref by', 'reffered by'],
                'Date': ['Dated', 'Date', 'DOC', 'DOD', 'DOA'],
                'Diagnosis': ['Diagnosis', 'Final Diagnosis', 'Principal/Secondary Diagnosis'],
                'Treatment Given': ['Treatment Given', 'On Examination', 'Examination'],
                'Summary': ['Summary', 'Past Treatment Given'],
                'MR Number': ['MR No', 'MR Number', 'MRNO '],
                'Blood Urea': ['Blood Urea', 'Urea in Blood'],
                'Serum Creatinine': ['serum creatinine', 'creatinine serum'],
                'Urine Sugar': ['urine sugar', 'sugar (urine)'],
                'Bile Pigment': ['bile pigment', 'pigment(bile)'],

                }

result_dict = defined_dict
result_dict = result_dict.fromkeys(result_dict, '')
for key in defined_dict.keys():
    for similar_keys in defined_dict[key]:
        q = 0
        para = [similar_keys.lower() + r":(.*) ", similar_keys.lower() + r" : (.*) ", similar_keys.lower()
                + r": (.*)", similar_keys.lower() + r": (.*)",
                similar_keys.lower() + r"( *)\n(.*)", similar_keys.lower() + r" (.*)",
                similar_keys.lower() + r"\n\n(.*)",
                similar_keys.lower() + r": (.*)"]
        # tring to find string matches and its responses this just written
        # on basis of observing possibilities of ocr
        for target in para:

            match = re.search(target, text.lower())
            if match:
                result = match.group(1)
                q = 1
                result_dict[key] = result
                break
            else:
                result = ""
        if q == 1:
            break

with open('output.json', 'w') as fp:
    json.dump(result_dict, fp)

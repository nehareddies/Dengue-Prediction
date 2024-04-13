from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('dengue_detection.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    temp = float(request.form['temp'])
    wbc = float(request.form['wbc'])
    hematocri = float(request.form['hematocri'])
    hemoglobin = float(request.form['hemoglobin'])
    platelet = float(request.form['platelet'])
    headache = request.form.get('headache')
    headache = 1 if headache == 'on' else 0
    pain_behind_eye = request.form.get('pain_behind_eye')
    pain_behind_eye = 1 if pain_behind_eye == 'on' else 0
    joint_muscle_aches = request.form.get('joint_muscle_aches')
    joint_muscle_aches = 1 if joint_muscle_aches == 'on' else 0
    metallic_taste_in_the_mouth = request.form.get('metallic_taste_in_the_mouth')
    metallic_taste_in_the_mouth = 1 if metallic_taste_in_the_mouth == 'on' else 0
    appetite_loss = request.form.get('appetite_loss')
    appetite_loss = 1 if appetite_loss == 'on' else 0
    abdominal_pain = request.form.get('abdominal_pain')
    abdominal_pain = 1 if abdominal_pain == 'on' else 0
    nausea_vomiting = request.form.get('nausea_vomiting')
    nausea_vomiting = 1 if nausea_vomiting == 'on' else 0
    diarrhoea = request.form.get('diarrhoea')
    diarrhoea = 1 if diarrhoea == 'on' else 0

    result = model.predict([[temp, wbc, headache, pain_behind_eye,joint_muscle_aches, metallic_taste_in_the_mouth,appetite_loss, abdominal_pain, nausea_vomiting, diarrhoea, hemoglobin, hematocri, platelet]])[0]
    if result==1:
        result = "Dengue Detection Reports show that you are more likely to be having Dengue!"
    else:
        result = "Dengue Detection Reports show that you are not likely to be having Dengue!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
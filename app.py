from math import expm1
from flask import Flask, jsonify, request,flash, render_template, json, current_app as app
# from tensorflow import keras
from keras.models import model_from_json
import os
from werkzeug.utils import secure_filename

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "model1.json")

json_file = open(json_url)
loaded_model_json = json_file.read()
json_file.close()
model_e2d2 = model_from_json(loaded_model_json)
# model_e2d2.load_weights("/model_weight1.h5")
model_e2d2.load_weights(os.path.join(SITE_ROOT, "model_weight1.h5"))


data1=[[[0.21917388, 0.05479303, 0.78811264, 0.15476044, 0.09047352,0.64862263],[0.22031076, 0.05601694, 0.78814626, 0.15512122, 0.09055088,0.6512382 ],[0.21968909, 0.05771291, 0.78814626, 0.1560363 , 0.09055106,0.647571]]]
ALLOWED_EXTENSIONS = {'txt', 'json'}


app = Flask(__name__)
@app.route('/model', methods=['GET', 'POST'])
def predict_cmd():
    data = request.json
    prediction = model_e2d2.predict(data['login'])
    prediction=prediction.reshape(-1)
    for i in range(len(prediction)):
        if(prediction[i] >= 0.5):
             prediction[i]=1
        else:
             prediction[i]=0
    return jsonify({"Prediction for comming day/s": str(prediction)})

@app.route('/', methods=['GET', 'POST'])
def index():
     data=""
     if request.method == 'POST':
     # check if the post request has the file part
          if 'file' not in request.files:
             return render_template('index.html', msg2="No File Part")
          file = request.files['file']
          if file.filename == '':
              return render_template('index.html', msg2="No File Selected")
          if file and allowed_file(file.filename):
               try:
                    data = file.read()
                    obj = json.loads(data)
                    prediction = model_e2d2.predict(obj['login'])
                    prediction=prediction.reshape(-1)
                    res=""
                    list=[]
                    for i in range(len(prediction)):
                         if(prediction[i] >= 0.5):
                              prediction[i]=1
                              res += "Prediction day" + str(i + 1) + ":" +  str(prediction[i]) + "<br>"
                              list.append(prediction[i].astype(int))
                         else:
                              prediction[i]=0
                              res += "Prediction day" + str(i + 1) + ":" +  str(prediction[i]) + "<br>"
                              list.append(prediction[i].astype(int))
                    return render_template('index.html', msg=(list))
               except:
                    return render_template('index.html', msg1="Bad Json File please Upload Json File again")
          else:
               return render_template('index.html', msg2="Not Supported File")
     elif request.method == 'GET':
            return render_template('index.html', msg="")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':  
    app.run(debug = True)  
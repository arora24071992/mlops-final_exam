from flask import Flask
from flask import request
from joblib import load

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<!-- hello --> <b> Hello, World!</b>"


# get x and y somehow    
#     - query parameter
#     - get call / methods
#     - post call / methods ** 

@app.route("/sum", methods=['POST'])
def sum():
    x = request.json['x']
    y = request.json['y']
    z = x + y 
    return {'sum':z}



@app.route("/predict", methods=['POST'])
def predict_digit():
    image = request.json['image']
    model_name = request.json['model_name']
    model = load(model_name)
    print("Model loaded")
    predicted = model.predict([image])
    return {"y_predicted":int(predicted[0])}
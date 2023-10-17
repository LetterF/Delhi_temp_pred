from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open("regression.pkl", "rb"))

def averageTemperature_pred(month, year=2018):
    start = 48
    end = start + (year-2017)*12 + (month-1)

    pred=model.predict(start=start, end=end)
    conf_int=model.get_prediction(start=start, end=end).conf_int()
    
    return [pred[-1],conf_int["lower meantemp"][-1],conf_int["upper meantemp"][-1]]
@app.route("/")

def homePage():
  return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
  int_features=[int(x) for x in request.form.values()]
  final=[np.array(int_features)]
  prediction=averageTemperature_pred(1)
  

if __name__ == "__main__":

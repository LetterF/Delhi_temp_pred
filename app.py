from flask import Flask, render_template, request
from logging import FileHandler,WARNING
import pickle
import numpy as np
app = Flask(__name__)
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

def averageTemperature_pred(month, year=2018):
    start = 48
    end = start + (year-2017)*12 + (month-1)

    pred=model.predict(start=start, end=end)
    conf_int=model.get_prediction(start=start, end=end).conf_int()
    
    return [pred.iloc[-1],conf_int["lower meantemp"].iloc[-1],conf_int["upper meantemp"].iloc[-1]]

model=pickle.load(open("regression.pkl", "rb"))


@app.route("/")
def homePage():
  return render_template("index.html")
@app.route("/predict", methods=["POST", "GET"])
def predict():
  int_features=[int(x) for x in request.form.values()]
  final=[np.array(int_features)]
  month = int(request.values.get("month"))
  year = int(request.values.get("year"))
  if month is None:
            month = "Not Submitted"
            return month
  if year is None:
            year = "Not Submitted"
            return year
  prediction=averageTemperature_pred(month, year)
  
  return render_template("index.html",result=(f"The average temperature in Delhi on {month} of {year} is {prediction[0]} \n with upper confidence interval of {prediction[2]} \n and lower confidence interval of {prediction[1]}"))
if __name__ == "__main__":
    app.run()
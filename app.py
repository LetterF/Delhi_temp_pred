from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open("predModel.pkl", "rb"))
@app.route("/")

def homePage():
  return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
  print(request.form)
  int_features=[int(x) for x in request.form.values()]
  final=[np.array(int_features)]
  print(int_features)
  print(final)
  prediction=model.predict()

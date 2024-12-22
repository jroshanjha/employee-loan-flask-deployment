from flask import Flask,render_template,jsonify
import pickle
import os
import joblib
import numpy as np 



# Application configuration:- 
app = Flask(__name__)

# Model configurations 
# Load the model 
# Load the model 
with open('model.pkl', 'rb') as model_file: 
    model = pickle.load(model_file)


@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True,port=8080)
    




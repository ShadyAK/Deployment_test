from flask import Flask,request,jsonify
import numpy as np
import json

app=Flask(__name__)

@app.route('/')
def home():
    return "WELCOME"
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=="POST":
        data=request.json
        print(type(data))
        return jsonify(data)
    
if __name__=='__main__':
    app.run(debug=True)            
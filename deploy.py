from flask import Flask,request,jsonify
import numpy as np
import json

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello Soumybeeeeerrrrrrrrrr"
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=="POST":
        data=request.json
        #print(type(data))
        return jsonify({"ASHWIN":"KAURAV"})
    else:
        return "HEMLO"
if __name__=='__main__':
    app.run(debug=True)            

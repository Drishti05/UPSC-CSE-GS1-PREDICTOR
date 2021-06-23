from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('predict.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Current=1
        NCERT=1
        Overlap=0
        Previous=1
        Reference=0
        Syllabus=0
         
        current=request.form['FIRST']
        if(current=='NO'):
            Current=1
        elif(current=='APPEARED IN 1 TO 4 EDITORIALS'):
            Current=2
        elif(current=='APPEARED IN 4-7 EDITORIALS OR IMPORTANT DAY'):
            Current=3
        elif(current=='APPEARED IN 7-10 EDITORIALS OR IN SCHEMES OR ANY INDEX'):
            Current=4  
        elif(current=='APPEARED IN MORE THAN 10 EDITORIALS OR NITI AYOG REPORT OR PROGRAM BY GOVERNMENT'):
            Current=5   
            
        ncert=request.form['SECOND']  
        if(ncert=='NO'):
            NCERT=1
        elif(ncert=='CLASS 6-8'):
            NCERT=2
        elif(ncert=='CLASS 9-10'):
            NCERT=3
        elif(ncert=='CLASS 11-12'):
            NCERT=4
            
            
        overlap=request.form['THIRD']   
        if(overlap=='NO'):
            Overlap=0 
        else:
            Overlap=1
            
        previous=request.form['FOURTH']
        if(previous=='NO'):
            Previous=1
        elif(previous=='PREVIOUS 10 YEARS'):
            Previous=2
        elif(previous=='PREVIOUS 5 YEARS'):
            Previous=3   
            
            
        reference=request.form['FIFTH']
        if(reference=='NO'):
            Reference=0 
        else:
            Reference=1
            
            
        
        syllabus=request.form['SIXTH']   
        if(syllabus=='NO'):
            Syllabus=0 
        else:
            Syllabus=1 
            
        Type_Ancient=0
        Type_Env=0
        Type_HG=0
        Type_Mod=0
        Type_PG=0
        Type_Soc=0
        Type_WH=0
        Type=request.form['SEVENTH']
        if(Type=='ART & CULTURE or MEDIEVAL'):
            Type_Ancient=1
        elif(Type=='ENVIRONMENT or ASTRONOMY or DISASTER'):
            Type_Env=1
        elif(Type=='HUMAN GEOGRAPHY or GLOBALIZATION'):
            Type_HG=1
        elif(Type=='MODERN OR POST INDEPENDENCE'):
            Type_Mod=1
        elif(Type=='PHYSICAL GEOGRAPHY or AGRICULTURE or WORLD GEOGRAPHY'):
            Type_PG=1
        elif(Type=='SOCIETY or WOMEN'):
            Type_Soc=1
        elif(Type=='WORLD HISTORY'):
            Type_WH=1 
        prediction=model.predict([[Current,NCERT,Overlap,Previous,Reference,Syllabus,Type_Ancient,Type_Env,Type_HG,Type_Mod,
                                   Type_PG,Type_Soc,Type_WH]])
        if (prediction==1):
            return render_template('index.html',THE_QUESTION_WILL_APPEAR_IN_THE_EXAM="YES IT CAN BE THERE IN THE EXAM")
        elif(prediction==0):
            return render_template('index.html',THE_QUESTION_WILL_APPEAR_IN_THE_EXAM="NO IT WILL NOT BE THERE IN THE EXAM".format(prediction))
        else:
            return render_template('index.html',THE_QUESTION_WILL_APPEAR_IN_THE_EXAM="CANNOT COMMENT ABOUT ITS APPEARANCE")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
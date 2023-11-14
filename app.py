from flask import Flask,redirect,url_for,render_template,request
import pickle 
import numpy as np

model=pickle.load(open('tr_model.sav','rb'))

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('manual.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        gender=int(request.form['gender'])
        age=int(request.form['age'])
        height=float(request.form['height'])
        exercise_duration=float(request.form['execise_duration'])
        heart_rate=float(request.form['heart_rate'])
        body_temp=float(request.form['body_temp'])
        print("gender is ",gender)
        print("age is ",age)
        print("height is ",height)
        print("exercise duration is ",exercise_duration)
        print("heart rate is ",heart_rate)
        print("body temp is ",body_temp)
        input_df= np.array([gender,age,height,exercise_duration,heart_rate,body_temp])
        input_df=input_df.reshape(1,-1)
        result=model.predict(input_df)
        return render_template('output.html',result=result)

"""@app.route('/send',methods=['POST','GET'])
def send():
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        mobile_no=request.form['mobile_no']
        query=request.form['query']
        print("first name is : ",first_name)
        print("last name is :",last_name)
        print("email of user is :",email)
        print("mobile no is :",mobile_no)
        print("query is :",query)
        return render_template('index.html',**locals())
"""
    
if __name__=='__main__':
    app.run(debug=True)
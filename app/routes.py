from flask import Flask, render_template, request, make_response
import plivo
from app import app


auth_id = "YOUR_AUTH_ID"
auth_token = "YOUR_AUTH_TOKEN"


p = plivo.RestAPI(auth_id, auth_token)   
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/call/', methods=['GET'])
def call():

    dialNumber1 = request.args.get('dialNumber1')
    global dialNumber2
    dialNumber2 = request.args.get('dialNumber2')

    # Make Calls
    params = {
    'from': '1800111108', # Caller Id
    'to' : dialNumber1, # User Number to Call	
    'answer_url' : "http://lets-talk.herokuapp.com/answer_url/",
    'answer_method' : 'GET'
    }
    response = p.make_call(params)

    print dialNumber1, dialNumber2, response
    return render_template('index.html', dialNumber1=dialNumber1, dialNumber2=dialNumber2)


@app.route('/answer_url/', methods=['GET'])
def answer_url():
    r = plivo.Response()
    
    # Add speak
    body = 'This is Plivo Lets Talk App.'
    params = {'loop':1}
    r.addSpeak(body, **params)

    #Add Dial Number
    d = r.addDial()
    d.addNumber(dialNumber2)
    
    response = make_response(r.to_xml())
    response.headers["Content-type"] = "text/xml"

    return response


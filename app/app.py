import os
import json

from flask import Flask
from flask import url_for, redirect, render_template, flash, g, session, request

from flask_bootstrap import Bootstrap

from firebase import firebase

app = Flask(__name__)
Bootstrap(app)

firebase = firebase.FirebaseApplication("https://mit-chennai.firebaseio.com", None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submission', methods=['GET', 'POST'])
def submission():
    name = request.form['name']
    email = request.form['email']
    email2 = request.form['email2']
    email3 = request.form['email3']

    sos, alarm, fall = False, False, False

    if request.form.get('sos'):
        sos = True
    if request.form.get('alarm'):
        alarm = True
    if request.form.get('fall'):
        fall = True


    data = {'name': name, 'email': {'1': email2, '2': email2, '3': email3}, 'modules': {'sos': sos, 'fall': fall, 'alarm': alarm}}
    # sent = json.dumps(data)
    firebase.put('', name, data)
    # firebase.post('', sent)

    return render_template('submission.html', name=name, email=email, email2=email2, email3=email3, sos=sos, fall=fall, alarm=alarm)
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
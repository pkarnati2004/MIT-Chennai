import os

from flask import Flask
from flask import url_for, redirect, render_template, flash, g, session, request

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    race = request.form['race']

    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
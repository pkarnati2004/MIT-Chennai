import os

from flask import Flask
from flask import url_for, redirect, render_template, flash, g, session

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
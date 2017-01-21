from flask import Flask
from flask import render_template, url_for, redirect, abort, session

app = Flask(__name__, static_url_path='/static')
# Serve static files like this: 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/docs/')
def docs():
    return render_template('docs.html')
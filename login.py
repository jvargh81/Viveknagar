import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
#import sqlite3

app = Flask(__name__)

#config 
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create sqlalchemy object.
db = SQLAlchemy(app)

from models import *

#login required decorator

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first!!')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route("/")
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET','POST'])

def login():
    error = None
    if request.method == 'POST' :
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again!!!'
        else:
            session['logged_in'] = True
            flash('You were just logged in!!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('You were just logged out!!')
    return redirect(url_for('login'))


if __name__ == '__main__' :
    app.run()
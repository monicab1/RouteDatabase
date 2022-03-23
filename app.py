#pylint: disable=invalid-name
#pylint: disable=missing-final-newline
#pylint: disable=line-too-long
#pylint: disable=unpacking-non-sequence
#pylint: disable=superfluous-parens
#pylint: disable=trailing-whitespace
#pylint: disable=wrong-import-order
#pylint: disable=unused-import
import os
import flask
import requests
import random
from flask import flash, redirect, url_for
from flask import request

from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists,delete

from dotenv import find_dotenv, load_dotenv

from movie import DrStrange,Spiderman,KingsMan

load_dotenv(find_dotenv())


app = flask.Flask(__name__)
secret_key=os.getenv("SECRET_KEY")
app.secret_key = secret_key

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #pass the app object into the DB


@app.route("/")
def index():
    """
    method 
    """
    return flask.render_template("index.html")



@app.route("/login")
def login():
    """
    method 
    """
    return flask.render_template("login.html")



@app.route("/movie_home")
def movie_home():
    """
    method
    """
    rand = random.randint(0,2)
    if (rand==0):
        (title,tagline,list1,image2) = DrStrange()
    elif (rand==1):    
        (title,tagline,list1,image2) = Spiderman()
    else:    
        (title,tagline,list1,image2) = KingsMan()    
    
    return flask.render_template("movie_home.html",title=title,tagline=tagline,list1=list1,image2=image2)

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
    debug=True)
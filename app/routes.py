#flask routes control what content is shown on what url depending on hot the user is accessing that url
# , what ubtton they've pressed, etc.

#the general structure of a flask route is a funtion with a decorator
#a decorator adds lines of code that run before and after the decorated function

#our first route:
#goal display the index.html file when use navigates to the base url ada 'http://127.0.0.1:500/'

#in order to do this we need a few tools
#1. we need to access to our app

from app import app  #import the app variable defined in __init__.py
 #2. we need the ability to show an html file at a specified url
 #render_template function
 #if your route's  job is to display an html page --> it's return value should be a call to rendor_template
from flask import render_template

@app.route('/') #decorator says:this function is a route of the flask app 'app' with the url endpoint '/'
def home():
    return render_template('index.html')

# a second route!
@app.route('/mcfc')
def mancity():
    return render_template('soccer.html')
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import (Flask, after_this_request, make_response, request,
                   send_from_directory, render_template)
from Generateur_stellaris_RP import app
import os
import shortuuid

UPLOAD_FOLDER = "./static/parties/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/Join')
def join():
    """Renders the join page."""
    return render_template(
        'Join.html',
        title='Join',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/Regles')
def regles():
    """Renders the rules page."""
    return render_template(
        'Regles.html',
        title='Regles',
        year=datetime.now().year,
        message='Voici les règles de notre petit jeu.',
        charset='utf-16'
    )

@app.route('/Create')
def create():
    """Renders the create page."""
    return render_template(
        'Create.html',
        title='Create',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/handle_create',methods=["POST"])
def handle_create():
    id_partie = shortuuid.uuid()
    result = {}
    result["avatar"] = {"id" : shortuuid.uuid(),"nombre":1 }
    result["empereur"] = {"id" : shortuuid.uuid(),"nombre":1 }

    if request.form["democratie"] != "0" and request.form["democratie"] != "":
        result["democratie"] = {"id":shortuuid.uuid(), "nombre":request.form["democratie"]}

    if request.form["predicateur"] != "0" and request.form["predicateur"] != "":
        result["predicateur"] = {"id":shortuuid.uuid(), "nombre":request.form["predicateur"],"id_avatar":result["avatar"]["id"]}

    if request.form["vivant"] != "0" and request.form["vivant"] != "":
        result["vivant"] = {"id":shortuuid.uuid(), "nombre":request.form["vivant"]}

    if request.form["vassal"] != "0" and request.form["vassal"] != "":
        result["vassal"] = {"id":shortuuid.uuid(), "nombre":request.form["vassal"],"id_empereur":result["empereur"]["id"]}

    if request.form["marchand"] != "0" and request.form["marchand"] != "":
        result["marchand"] = {"id":shortuuid.uuid(), "nombre":request.form["marchand"]}

    return(result)
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import (Flask, after_this_request, make_response, request,
                   send_from_directory, render_template)
from Generateur_stellaris_RP import app
import os
import shortuuid
import json
import random
import time

UPLOAD_FOLDER = "Generateur_stellaris_RP/static/games/"
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
        title='Rejoindre une partie',
        year=datetime.now().year,
        message="Veuillez entrer l'ID de votre partie"
    )

@app.route('/Regles')
def regles():
    """Renders the rules page."""
    return render_template(
        'Regles.html',
        title='Regles',
        year=datetime.now().year,
        message='Voici les règles de notre petit jeu.',
    )

@app.route('/Create')
def create():
    """Renders the create page."""
    return render_template(
        'Create.html',
        title='Création de la partie',
        year=datetime.now().year,
        message='Il y a également un avatar et un empereur qui sont ajoutés automatiquement'
    )

@app.route('/handle_create',methods=["POST"])
def handle_create():
    id_partie = shortuuid.uuid()
    result = {}
    result["Avatar_de_la_fin_des_temps"] = {"id" : shortuuid.uuid(),"nombre":1 }
    result["Emperor_of_the_mankind"] = {"id" : shortuuid.uuid(),"nombre":1 }

    if request.form["democratie"] != "0" and request.form["democratie"] != "":
        result["Defenseur_de_la_democratie"] = {"id":shortuuid.uuid(), "nombre":request.form["democratie"]}

    if request.form["predicateur"] != "0" and request.form["predicateur"] != "":
        result["Predicateur_de_la_fin_des_temps"] = {"id":shortuuid.uuid(), "nombre":request.form["predicateur"],"id_avatar":result["Avatar_de_la_fin_des_temps"]["id"]}

    if request.form["vivant"] != "0" and request.form["vivant"] != "":
        result["Protecteur_du_vivant"] = {"id":shortuuid.uuid(), "nombre":request.form["vivant"]}

    if request.form["vassal"] != "0" and request.form["vassal"] != "":
        result["Vassal_de_l'empereur"] = {"id":shortuuid.uuid(), "nombre":request.form["vassal"],"id_empereur":result["Emperor_of_the_mankind"]["id"]}

    if request.form["marchand"] != "0" and request.form["marchand"] != "":
        result["Marchand_universel"] = {"id":shortuuid.uuid(), "nombre":request.form["marchand"]}
     
    with open(app.config["UPLOAD_FOLDER"] + str(id_partie), 'w') as f:
        json.dump(result, f, indent=4)
    
    return render_template(
        'game_creation.html',
        title='Création de partie',
        year=datetime.now().year,
        message='Votre partie a bien été créé',
        id = id_partie
    )
@app.route('/handle_join',methods=["POST"])
def handle_join():
    time.sleep(random.random())

    id_partie = request.form["id"]
    try:
        f = open(app.config["UPLOAD_FOLDER"] + id_partie)
        role_restant = json.load(f)
    except:
        return render_template(
        'error_game.html',
        title='Partie innexistante ou fermé',
        year=datetime.now().year,
        message='Veuillez créer une partie ou en rejoindre une valide')

    role, infos = random.choice(list(role_restant.items()))

    id_joueur = infos["id"]
    try:
        id_avatar = infos["id_avatar"]
    except:
        id_avatar = ""

    try:
        id_empereur = infos["id_empereur"]
    except:
        id_empereur = ""

    role_restant [role]["nombre"] = int(role_restant[role]["nombre"]) - 1 #On enlève une place restante dans les roles

    if role_restant[role]["nombre"] == 0: #Si il y a plus de role on le suprime 
        role_restant.pop(role)
    with open(app.config["UPLOAD_FOLDER"] + str(id_partie), 'w') as f:
        json.dump(role_restant, f, indent=4) #On enregistre les modficiations

    @after_this_request
    def remove_game(response):

        if len(role_restant) == 0:
            os.remove(app.config["UPLOAD_FOLDER"] + id_partie)
        return(response)

    return render_template(
        'game_join.html',
        title='Voici votre role:',
        year=datetime.now().year,
        message='Id de la partie:' + str(id_partie),
        id = id_joueur,
        role = role,
        id_avatar = id_avatar,
        id_empereur = id_empereur
    )

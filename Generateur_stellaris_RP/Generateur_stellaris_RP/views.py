"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Generateur_stellaris_RP import app

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
    """Renders the contact page."""
    return render_template(
        'Join.html',
        title='Join',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/Regles')
def regles():
    """Renders the contact page."""
    return render_template(
        'Regles.html',
        title='Regles',
        year=datetime.now().year,
        message='Voici les règles de notre petit jeu.',
        charset='utf-16'
    )

@app.route('/Create')
def create():
    """Renders the about page."""
    return render_template(
        'Create.html',
        title='Create',
        year=datetime.now().year,
        message='Your application description page.'
    )

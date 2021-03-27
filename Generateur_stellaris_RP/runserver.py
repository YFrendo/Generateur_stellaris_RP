"""
This script runs the Generateur_stellaris_RP application using a development server.
"""

from os import environ
from Generateur_stellaris_RP import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT)

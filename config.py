import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Connect to the database
# username : omar , Password : 010 
SQLALCHEMY_DATABASE_URI = 'postgres://omar:010@localhost:5432/fyyur'

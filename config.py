# File Name: Config.py
# Author: Jesse Malinen
# Description: DB Config

class Config:
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ap:ap@localhost50435/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
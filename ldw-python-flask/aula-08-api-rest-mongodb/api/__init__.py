from flask import Flask
#Importando o pymongo
from flask_pymongo import PyMongo
#Import o Flask-Restful
from flask_restful import Api
#Importa o Marshmallow
from flask_marshmallow import Marshmallow

#Carregando flask
app=Flask(__name__)

#Carregando o Marshmallow
ma = Marshmallow(app)

#Configaração do Flak com o mongo
app.config["MONGO_URI"]='mongodb://localhost:27017/api-movies'

#Carregando Flask-Restful
api=Api(app)

#Carregando o pymongo
mongo=PyMongo(app)

#Importando os recursos (Precisa ser aqui)
from .resources import movies_resources



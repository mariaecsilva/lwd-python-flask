#Importar o Flask do pacote api
from api import app, mongo
#Importa a classe Movie
from api.models.movie_model import Movie
#Importa o service
from api.services import movie_service
from flask_marshmallow import Marshmallow

#Rodando a aplicação
if __name__ == "__main__":
        #Criar coleção no banco mongo
    with app.app_context():
        if 'movies' not in mongo.db.list_collection_names():
            movie=Movie(
                title='',
                description='',
                year=0
            )
            movie_service.add_movie(movie)  
    app.run(host="localhost", port="5000", debug="True")


from api import mongo
from ..models import movie_model
from bson import ObjectId

def add_movie(movie):
    result = mongo.db.movies.insert_one({
    #banco mongo db
        'title' : movie.title,
        'description' : movie.description,
        'year': movie.year
    })

    #Buscar filme 
    new_movie = mongo.db.movies.find_one({'_id' : result.inserted_id})
    return new_movie

#Método listar
#Métodos estáticos não precisam de instância
@staticmethod
def get_movies():
    return list(mongo.db.movies.find())

#Método para excluir
@staticmethod
def delete_movie(id):
    mongo.db.movies.delete_one({'_id' : ObjectId(id)})

#Método para listar um único filme
def get_movie_by_id(id):
    return mongo.db.movie.find_one({'_id' : ObjectId(id)})
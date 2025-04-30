#importando a classe Resorce do Flask-Restful
from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import movie_schema
from ..models import movie_model
from ..services import movie_service

class MovieList(Resource):
    def get(self):
        #buscando no banco
        movies=movie_service.get_movies()
        mv = movie_schema.MovieSchema(many=True)
        return make_response(mv.jsonify(movies), 200)
    
    def post(self):
        mv=movie_schema.MovieSchema()
        validate=mv.validate(request.json)
        #tratando se a validação falhar
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            title = request.json["title"]
            description = request.json["description"]
            year = request.json["year"]

            new_movie=movie_model.Movie(title=title, description=description, year=year)
            result = movie_service.add_movie(new_movie)
            res = mv.jsonify(result)
            return make_response(res, 201)
        
class MovieDetail(Resource):
    def delete(self,id):
        movie = movie_service.get_movie_by_id(id)
        if movie is None:
            return make_response(jsonify("Filme não encontrado!"), 404)
        movie_service.delete_movie(id)
        return make_response(jsonify("Filme excluido com sucesso"), 204)

api.add_resource(MovieList, '/movies')
api.add_resource(MovieDetail, '/movie/<id>')

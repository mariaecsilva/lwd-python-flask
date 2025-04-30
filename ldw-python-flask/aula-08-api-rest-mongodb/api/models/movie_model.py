from api import mongo

class Movie():
    def __init__(self, title, description, year):
        self.title = title
        self.description = description
        self.year = year
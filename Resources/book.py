from flask_restful import Resource
from models import Book

class BookResources(Resource):
    def get(self,id=None):
        if id == None:
            books = Book.query.all()

            return books
        else:
            category = Book.query.filter_by(id=id).first()
            # print(Book)

            return category



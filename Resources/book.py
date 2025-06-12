from flask_restful import Resource
from models import Book, db 
from flask import request
class BookResources(Resource):
    def get(self,id=None):
        if id == None:
            books = Book.query.all()

            return books
        else:
            books = Book.query.filter_by(id=id).first()
            # print(Book)

            return books
    

    # CRUD method for post operation
    def post(self):
        # Gets Json data from the request
        data = request.get_json()

        # Next check if all the required fields are present

        if not data or 'title' not in data or 'author' not in data or 'description' not in data or 'category_id' not in data:
            return {
                "message": "Title, author, description, and category_id are required"
            },400
        
        # Then create a new book instance

        new_book = Book(
            title=data["title"],
            author=data["author"],
            description=data["description"],
            category_id = data["category_id"],
            created_at=db.func.current_timestamp() #Current timestamp
        )

        # Finally add commit to the database

        db.session.add(new_book)

        db.session.commit()

        # Return the created book

        return new_book.to_dict(), 200




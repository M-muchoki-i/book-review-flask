""" "
Book Review Sytstem

"""

# entities
# user- id, username, email, password
# book- id, title, author, description, user_id
# Review- id, content, rating user_id, book_id
# Category- id, name

from flask import Flask
from flask_restful import  Api,Resource
from flask_migrate import Migrate
from models import db
from Resources.categories import CategoryResource
from Resources.book import BookResources
from Resources.user import UserResources

app = Flask(__name__)


# configuring our flask app through the config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"

# link flask-restful with flask
api = Api(app)

migrate = Migrate(app, db)

# link our db to the flask app
db.init_app(app)


# C.R.U.D for categories
# @app.post("/categories")
# def create_category():
#     return {"message": "Category created"}


# @app.get("/categories")
# def get_all_category():
#     return {}


# @app.get("/categories/<id>")
# def get_category(id):
#     return {}


# @app.patch("/categories/<id>")
# def update_category(id):
#     return {"message": "Category updated"}


# @app.delete("/categories/<id>")
# def delete_category(id):
#     return {"message": "Category deleted"}


# # C.R.U.D. for user


# @app.post("/users")
# def create_user():
#     return {"message": "user sucessfull created"}


# @app.get("/users")
# def get_all_users():
#     return {}


# @app.get("/users/<id>")
# def get_users(id):
#     return {}


# @app.patch("/users/<id>")
# def update_users(id):
#     return {"message": "user updated"}


# @app.delete("/users/<id>")
# def delete_user(id):
#     return {"message": "user deleted"}


# # C.R.U.D for book


# @app.post("/books")
# def create_book():
#     return {"message": "book added sucessfully "}


# @app.get("/books")
# def get_all_books():
#     return {}


# @app.get("/books/<id>")
# def get_books(id):
#     return {}


# @app.patch("/books/<id>")
# def update_books(id):
#     return {"message": "book updated"}


# @app.delete("/books/<id>")
# def delete_book(id):
#     return {"message": "book deleted"}


# # C.R.U.D for  reviews


# @app.post("/reviews")
# def create_new_review():
#     return {"message": "review sucessfull createded"}


# @app.get("/reviews")
# def get_all_reviews():
#     return {}


# @app.get("/reviews/<id>")
# def get_reviews(id):
#     return {}


# @app.patch("/reviews/<id>")
# def update_reviews(id):
#     return {"message": "review updated"}


# @app.delete("/reviews/<id>")
# def delete_reviews(id):
#     return {"message": "review deleted"}


api.add_resource(CategoryResource, "/categories", "/categories/<int:id>")
api.add_resource(BookResources, "/books", "/books/<int:id>")
api.add_resource(UserResources, "/users", "/users/<int:id>")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
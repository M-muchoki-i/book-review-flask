from flask_restful import Resource
from models import Category

class CategoryResource(Resource):
    # /categories
    # /categories/<id>
    def get(self, id=None):
        if id == None:
            categories = Category.query.all()

            return categories
        else:
            category = Category.query.filter_by(id=id).first()
            # print(category)

            return category


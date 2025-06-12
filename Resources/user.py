from flask_restful import Resource
from models import User

class UserResources(Resource):
    def get(self, id=None):
        if id == None:
            users = User.query.all()

            return users
        else:
            users = User.query.filter_by(id=id).first()

            return users

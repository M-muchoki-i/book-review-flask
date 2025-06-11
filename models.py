
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata=MetaData()
db=SQLAlchemy(metadata=metadata)

class Category(db.Model):
    __tablename__= "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP) 
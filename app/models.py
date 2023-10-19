from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

class User(db.Model,SerializerMixin):
    __tablename__='users'
    serialize_rules = ('-cars.user')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False, unique=True)

    cars = db.relationship('Car',backref='user')

    def __repr__(self):
        return f'<The current user id {self.name}>'

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
        }



class Car(db.Model,SerializerMixin):
    __tablename__='cars'
    serialize_rules = ('-user.cars')

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)

    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<The car you are checking is {self.model}>'

    def to_dict(self):
        return {
            'id':self.id,
            'model':self.model,
            'user_id': self.user_id,
        }
from flask import url_for
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Integer)





    def to_dict(self):
        data = {
            "id": self.id,
            "email": self.email,
            "rating": self.rating
        }
        return data
    


    def from_dict(self, data):
        for field in ['email', 'rating']:
            if field in data:
                setattr(self, field, data[field])




class Picture(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String(200))



    def to_dict(self):
        data = {
            "id": self.id,
            "url": self.url
        }
        return data

    def from_dict(self, data):
        for i in ['url']:
            if i in data:
                setattr(self, i, data[i])
from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.Text())
    created_on = db.Column(db.DateTime())
    
    def __init__(self,first_name,last_name,gender,email,location,biography):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email 
        self.location = location
        self.biography = biography

    def __repr__(self):
        return '<User %r>' % (self.username)

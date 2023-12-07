from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    ratings = db.relationship('Ratings', backref=db.backref('ratings'), lazy=True)
    

    def __repr__(self):
        return f'Students({self.name}, {self.surname}, {self.group}, {self.email})'
    
class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return f'Faculty({self.id}, {self.name_fac})'
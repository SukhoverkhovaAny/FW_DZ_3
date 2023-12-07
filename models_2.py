from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    author = db.relationship('Books', backref=db.backref('authors'), lazy=True)


    def __repr__(self):
        return f'Autors({self.name}, {self.surname})'
    
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year_pub = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    

    def __repr__(self):
        return f'Books({self.name}, {self.year_pub}, {self.copies})'
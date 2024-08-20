from db import db

class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(80), nullable=False)
    director = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String(80), nullable=False)
    runtime = db.Column(db.String(80), nullable=False)
    original_language = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)
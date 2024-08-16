from db import db

class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True) # ok 
    title = db.Column(db.String(80), nullable=False) # ok
    director = db.Column(db.String(80), nullable=False) # ok
    year = db.Column(db.Integer, nullable=False) # ok
    genres = db.Column(db.String(80), nullable=False) # ok
    runtime = db.Column(db.String(80), nullable=False) # ok
    original_language = db.Column(db.String(80), nullable=False) # ok
    rating = db.Column(db.String(80), nullable=False)
    
    # @property
    # def rating(self):
    #     return f"{self.rating_stored}/5" if self.rating_stored is not None else None

    # @rating.setter
    # def rating(self, value):
    #     try:
    #         self.rating_stored = int(value)
    #     except ValueError:
    #         raise ValueError("Rating must be an integer")
        
    # @property
    # def formatted_rating(self):
    #     return f"{self.rating}/5" if self.rating is not None else None

    # def __repr__(self):
    #     return f"<Movie(title='{self.title}',
    #               director='{self.director}',
    #               year='{self.year}',
    #               genres='{self.genres}',
    #               runtime='{self.runtime}',
    #               original_language='{self.original_language}',
    #               rating='{self.formatted_rating}')>"

    # @property
    # def formatted_rating(self):
    #     return "{}/5".format(self.rating) if self.rating is not None else None

    # def __repr__(self):
    #     return "<Movie(title='{}', director='{}', year={}, genres='{}', runtime='{}', original_language='{}', rating='{}')>".format(
    #         self.title, self.director, self.year, self.genres, self.runtime, self.original_language, self.formatted_rating
    #     )

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'director': self.director,
    #         'year': self.year,
    #         'genres': self.genres,
    #         'runtime': self.runtime,
    #         'original_language': self.original_language
    #     }
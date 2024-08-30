from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from schemas import MovieSchema, MovieUpdateSchema, MultipleMoviesSchema

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, or_
from db import db
from models import MovieModel
from resources.resources_methods import ValidationFunctions
from resources.resources_methods import MovieExceptions

MAX_MOVIES_LIMIT = 200

# Blueprint for the movie resource, allowing us to define routes
blp = Blueprint("movies", __name__, description="Operations on movies")

# Resource for fetching movies from a specific decade
@blp.route("/movie/decade/<string:decade>")
class MovieDecade(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, decade):
        if decade.endswith("s") and decade.count("s") == 1:
            try:
                decade_number = int(''.join(filter(str.isdigit, decade)))
                if decade_number % 10 == 0:
                    movies = MovieModel.query.filter((MovieModel.year >= decade_number) & 
                                                     (MovieModel.year < (decade_number+10))).all()
                    if movies:
                        return movies
                    abort(404, message="Movies not found for the specified decade")
                else:
                    abort(400, message="Invalid decade format")
            except ValueError:
                abort(400, message="Invalid decade format")
        else:
            abort(400, message="Invalid decade format")

# Resource for sorting movies by rating
@blp.route("/movie/rating/sorting/<string:sort_direction>")
class MovieRatingSorting(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, sort_direction):
        movies = MovieModel.query.all()
        if sort_direction == "asc":
            movies.sort(key=lambda x: int(x.rating[0]))
        elif sort_direction == "desc":
            movies.sort(key=lambda x: int(x.rating[0]), reverse=True)
        else:
            abort(400, message="Error, invalid sort direction. Use 'asc' or 'desc'.")
        return movies

# Resource for sorting movies by year
@blp.route("/movie/year/sorting/<string:sort_direction>")
class MovieYearSorting(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, sort_direction):
        movies = MovieModel.query.all()
        if sort_direction == "asc":
            movies.sort(key=lambda x: x.year)
        elif sort_direction == "desc":
            movies.sort(key=lambda x: x.year, reverse=True)
        else:
            abort(400, message="Error, invalid sort direction. Use 'asc' or 'desc'.")
        return movies

# Resource for sorting movies by title
@blp.route("/movie/title/sorting/<string:sort_direction>")
class MovieTitleSorting(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, sort_direction):
        movies = MovieModel.query.all()
        if sort_direction == "asc":
            movies.sort(key=lambda x: x.title)
        elif sort_direction == "desc":
            movies.sort(key=lambda x: x.title, reverse=True)
        else:
            abort(400, message="Error, invalid sort direction. Use 'asc' or 'desc'.")
        return movies

# Resource for sorting movies by ID
@blp.route("/movie/id/sorting/<string:sort_direction>")
class MovieIdSorting(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, sort_direction):
        movies = MovieModel.query.all()
        if sort_direction == "asc":
            movies.sort(key=lambda x: x.id)
        elif sort_direction == "desc":
            movies.sort(key=lambda x: x.id, reverse=True)
        else:
            abort(400, message="Error, invalid sort direction. Use 'asc' or 'desc'.")
        return movies

# Resource for sorting movies by runtime
@blp.route("/movie/runtime/sorting/<string:sort_direction>")
class MovieRuntimeSorting(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, sort_direction):
        movies = MovieModel.query.all()
        if sort_direction == "asc":
            movies.sort(key=lambda x: int(x.runtime.split()[0]))
        elif sort_direction == "desc":
            movies.sort(key=lambda x: int(x.runtime.split()[0]), reverse=True)
        else:
            abort(400, message="Error, invalid sort direction. Use 'asc' or 'desc'.")
        return movies

# Resource for fetching movies by their original language
@blp.route("/movie/original_language/<string:original_language>")
class MovieOriginalLanguage(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, original_language):
        original_language = original_language.title()
        movies = MovieModel.query.filter(MovieModel.original_language == original_language).all()
        if movies:
            return movies
        abort(404, message="Movies not found for the specified language")

# Resource for fetching movies by year
@blp.route("/movie/year/<string:year>")
class MovieYear(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, year):
        movies = MovieModel.query.filter(MovieModel.year == year).all()
        if movies:
            return movies
        abort(404, message="Movies not found for the specified year")

# Resource for fetching movies by director
@blp.route("/movie/director/<string:director>")
class MovieDirector(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, director):
        director = director.title()
        movies = MovieModel.query.filter(MovieModel.director == director).all()
        if movies:
            return movies
        abort(404, message="Movies not found for the specified director")

# Resource for fetching movies by title
@blp.route("/movie/title/<string:title>")
class MovieTitle(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, title):
        title = title.title()
        movies = MovieModel.query.filter(MovieModel.title == title).all()
        if movies:
            return movies
        abort(404, message="Movies not found for the specified title")

# Resource for fetching movies by genre
@blp.route("/movie/genre/<string:genre>")
class MovieGenre(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self, genre):
        # genre = genre.title()
        movies = MovieModel.query.filter(or_(MovieModel.genres == genre,
                                             MovieModel.genres.startswith(f"{genre},"),
                                             MovieModel.genres.contains(f",{genre},"), 
                                             MovieModel.genres.endswith(f",{genre}"))).all()
        if movies:
            return movies
        abort(404, message="Movies not found for the specified genre")

# Resource for fetching, deleting, or updating a movie by ID
@blp.route("/movie/<string:movie_id>")
class MovieId(MethodView):
    @blp.response(200, MovieSchema)
    @jwt_required(fresh=False)
    def get(self, movie_id):
        return MovieModel.query.get_or_404(movie_id)

    @jwt_required(fresh=True)
    def delete(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return {"message": "Movie deleted"}, 200
    
    @blp.arguments(MovieUpdateSchema)
    @blp.response(200, MovieSchema)
    @jwt_required(fresh=True)
    def put(self, movie_data, movie_id):
        movie_data = ValidationFunctions.title_dict(movie_data)
        if MovieModel.query.filter(and_(MovieModel.title == movie_data["title"],
                                        MovieModel.director == movie_data["director"],
                                        MovieModel.year == movie_data["year"])).first():
            abort(409, message="This movie already exists")
        elif movie_data["year"] < 1895:
            abort(400, message="The year is not correct")
        elif not(ValidationFunctions.validate_director_input(movie_data["director"])):
            abort(400, message="The format of the director's name is not correct")
        elif not(ValidationFunctions.validate_original_language_input(movie_data["original_language"])):
            abort(400, message="The format of the original language is not valid")
        elif not(ValidationFunctions.validate_title_input(movie_data["title"])):
            abort(400, message="The format of the title is not valid")
        elif not(ValidationFunctions.validate_genre_input(movie_data["genres"])):
            abort(400, message="The format of the genres is not valid")
        elif not(ValidationFunctions.validate_rating_input(movie_data["rating"])):
            abort(400, message="The format of the rating is not valid")
        elif not(ValidationFunctions.validate_runtime_input(movie_data["runtime"])):
            abort(400, message="The format of the runtime is not valid")

        movie = MovieModel.query.get(movie_id)
        if movie:
            movie.title = movie_data["title"]
            movie.director = movie_data["director"]
            movie.year = movie_data["year"]
            movie.genres = movie_data["genres"]
            movie.runtime = movie_data["runtime"]
            movie.original_language = movie_data["original_language"]
            movie.rating = movie_data["rating"]
            db.session.commit()
            response = movie, 200 # Updated resource
        else:
            new_movie = MovieModel(**movie_data)
            db.session.add(new_movie)
            db.session.commit()
            response = new_movie, 201 # Created new resource
        
        return response

# Resource for adding a single movie
@blp.route("/addmovie")
class AddMovie(MethodView):
    @blp.arguments(MovieSchema)
    @blp.response(201, MovieSchema)
    @jwt_required(fresh=True)
    def post(self, movie_data):
        try:
            added_movie = AddSingleMovie.add_single_movie(movie_data)
        except MovieExceptions.MovieAlreadyExistsError as e:
                abort(409, message=str(e))
        except (MovieExceptions.InvalidYearError,
                MovieExceptions.InvalidDirectorInputError,
                MovieExceptions.InvalidLanguageInputError,
                MovieExceptions.InvalidTitleInputError,
                MovieExceptions.InvalidGenreInputError,
                MovieExceptions.InvalidRatingInputError,
                MovieExceptions.InvalidRuntimeInputError) as e:
            abort(400, message=str(e))
        except MovieExceptions.DatabaseError as e:
            abort(500, message=str(e))
        except Exception as e:
            abort(500, message="An unknown error occurred")
        
        return added_movie, 201

# Resource for fetching or deleting all movies, or bulk adding movies
@blp.route("/movielist")
class MovieList(MethodView):
    @blp.response(200, MovieSchema(many=True))
    @jwt_required(fresh=False)
    def get(self):
        return MovieModel.query.all()
    
    @jwt_required(fresh=True)
    def delete(self):
        movies = MovieModel.query.all()

        if movies:
            for movie in movies:
                db.session.delete(movie)
            db.session.commit()
        else:
            abort(404, message="There aren't any movies")
        
        return {"message": "Movies deleted"}, 200
    
    @blp.arguments(MovieSchema(many=True))
    @blp.response(201, MultipleMoviesSchema)
    @jwt_required(fresh=True)
    def post(self, movies_data):
        if len(movies_data) > MAX_MOVIES_LIMIT:
            abort(400, message=f"You can only add up to {MAX_MOVIES_LIMIT} movies at a time. Now are {len(movies_data)}")

        added_movies = []
        errors = []
        
        for movie_data in movies_data:
            try:
                added_movie = AddSingleMovie.add_single_movie(movie_data)
                added_movies.append(added_movie)
            except (MovieExceptions.MovieAlreadyExistsError,
                    MovieExceptions.InvalidYearError,
                    MovieExceptions.InvalidDirectorInputError,
                    MovieExceptions.InvalidLanguageInputError,
                    MovieExceptions.InvalidTitleInputError,
                    MovieExceptions.InvalidGenreInputError,
                    MovieExceptions.InvalidRatingInputError,
                    MovieExceptions.InvalidRuntimeInputError,
                    MovieExceptions.DatabaseError) as e:
                errors.append(f"Error adding movie '{movie_data['title']}': {str(e)}")
            except Exception as e:
                errors.append(f"An unknown error occurred adding the movie: {movie_data['title']}")

        if errors and added_movies:
            return {"movies": added_movies, "error_messages": errors}, 207
        elif errors:
            return {"error_messages": errors}, 400
        else:
            return {"movies": added_movies}, 201

# Utility class for adding a single movie
class AddSingleMovie():
    @staticmethod
    def add_single_movie(movie_data):
        movie_data = ValidationFunctions.title_dict(movie_data)
        if MovieModel.query.filter(and_(MovieModel.title == movie_data["title"],
                                        MovieModel.director == movie_data["director"],
                                        MovieModel.year == movie_data["year"])).first():
            raise MovieExceptions.MovieAlreadyExistsError()
        elif movie_data["year"] < 1895:
            raise MovieExceptions.InvalidYearError()
        elif not ValidationFunctions.validate_director_input(movie_data["director"]):
            raise MovieExceptions.InvalidDirectorInputError()
        elif not ValidationFunctions.validate_original_language_input(movie_data["original_language"]):
            raise MovieExceptions.InvalidLanguageInputError()
        elif not ValidationFunctions.validate_title_input(movie_data["title"]):
            raise MovieExceptions.InvalidTitleInputError()
        elif not ValidationFunctions.validate_genre_input(movie_data["genres"]):
            raise MovieExceptions.InvalidGenreInputError()
        elif not ValidationFunctions.validate_rating_input(movie_data["rating"]):
            raise MovieExceptions.InvalidRatingInputError()
        elif not ValidationFunctions.validate_runtime_input(movie_data["runtime"]):
            raise MovieExceptions.InvalidRuntimeInputError()

        movie = MovieModel(**movie_data)
        try:
            db.session.add(movie)
            db.session.commit()
        except SQLAlchemyError:
            raise MovieExceptions.DatabaseError()
    
        return movie
# import uuid
# import models
import os

from flask import Flask, request, jsonify
from flask_smorest import abort, Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from datetime import timedelta

from blocklist import BLOCKLIST
from db import db

from resources.movie import blp as MovieBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["PROPAGATE EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Movies API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # the secret key set here, "fabio", is not very safe
    # Instead you should generate a long and random secret key using something like 
    # import secrets

    # def generate_secret_key(length):
    #     return secrets.token_urlsafe(length)

    # # Generate a secret key with a specified length (e.g., 32 bytes)
    # secret_key = generate_secret_key(32)
    # print("Generated Secret Key:", secret_key)

    app.config["JWT_SECRET_KEY"] = "cJpieIQE7fZh-5Ajr-iT_CTMcmAPWzvCd7l7gYQTnYk"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=3)  # Default is 15 minutes
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(minutes=5)  # Default is 30 days
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (jsonify({"description": "The token has been revoked.", "error": "token_revoked"}), 401)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (jsonify({"message": "The token has expired.", "error": "token_expired"}), 401)
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (jsonify({"message": "Signature verification failed.", "error": "invalid_token"}), 401)
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (jsonify({"description": "Request does not contain an access token.", "error": "authorization_required"}), 401)
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (jsonify({"description": "The token is not fresh.", "error": "fresh_token_required"}), 401)
    
    # with app.app_context():
    #    db.create_all()

    api.register_blueprint(MovieBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

# Flask app initialization and running
# devo provare se funziona, posso anche fare senza
# if __name__ == '__main__':
#     create_app()




# @app.get("/movie")  # http://127.0.0.1:5001/movie
# def get_movies():
#     return {"movies": movies}


# @app.post("/movie")
# def add_movie():
#     request_data = request.get_json()
#     new_movie = {"Title": request_data["Title"],
#                  "Director": request_data["Director"],
#                  "Year": request_data["Year"],
#                  "Genres": request_data["Genres"],
#                  "Runtime": request_data["Runtime"],
#                  "Original language": request_data["Original language"]}
#     movies.append(new_movie)
#     return new_movie, 201

# @app.get("/movie/<string:title>")
# def get_movie(title):
#     for movie in movies:
#         if movie["Title"] == title:
#             return movie
#     return {"message": "Movie not found"}, 404
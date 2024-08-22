from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, create_refresh_token, get_jwt_identity
import jwt
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema
from blocklist import BLOCKLIST
from refresh_token_store import REFRESH_TOKEN_STORE

# Blueprint for user operations
blp = Blueprint("Users", "users", description="Operations on users")

# User registration endpoint
@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        # Check if the username already exists
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        # Hash the password and create a new user
        user = UserModel(username=user_data["username"], password=pbkdf2_sha256.hash(user_data["password"]))
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201

# User login endpoint
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        # Verify the user's credentials
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            # Create tokens upon successful login
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            # Store the refresh token
            REFRESH_TOKEN_STORE[user.id] = refresh_token

            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        
        # Abort if credentials are invalid
        abort(401, message="Invalid credentials.")

# User logout endpoint
@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required(fresh=True)
    def post(self):
        # Get the current user's ID
        user_id = get_jwt_identity()
        stored_refresh_token = REFRESH_TOKEN_STORE.get(user_id)
        
        # Invalidate the access token by adding it to the blocklist
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        
        # Invalidate the refresh token as well
        refresh_jti = jwt.decode(stored_refresh_token, options={"verify_signature": False})["jti"]
        BLOCKLIST.add(refresh_jti)
        REFRESH_TOKEN_STORE.pop(user_id, None)

        return {"message": "Successfully logged out"}, 200

# Token refresh endpoint
@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        # Generate a new access token
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        return {"access_token": new_token}, 200
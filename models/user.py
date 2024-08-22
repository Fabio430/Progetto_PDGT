from db import db

# Database model for users
class UserModel(db.Model):
    __tablename__ = "users" # Table name in the database

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
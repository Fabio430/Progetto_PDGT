from marshmallow import Schema, fields

# Schema for validating and serializing/deserializing Movie objects
class MovieSchema(Schema):
    id = fields.Int(dump_only=True) # Only used for output
    title = fields.Str(required=True)
    director = fields.Str(required=True)
    year = fields.Int(required=True)
    genres = fields.Str(required=True)
    runtime = fields.Str(required=True)
    original_language = fields.Str(required=True)
    rating = fields.Str(required=True)

# Schema for updating Movie objects (all fields are optional)
class MovieUpdateSchema(Schema):
    title = fields.Str()
    director = fields.Str()
    year = fields.Int()
    genres = fields.Str()
    runtime = fields.Str()
    original_language = fields.Str()
    rating = fields.Str()

# Schema for handling multiple movies and potential error messages
class MultipleMoviesSchema(Schema):
    movies = fields.List(fields.Nested(MovieSchema), required=True)
    error_messages = fields.List(fields.Str(), required=False)

# Schema for validating and serializing/deserializing User objects
class UserSchema(Schema):
    id = fields.Int(dump_only=True) # Only used for output
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True) # Passwords are handled securely
from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    director = fields.Str(required=True)
    year = fields.Int(required=True)
    genres = fields.Str(required=True)
    runtime = fields.Str(required=True)
    original_language = fields.Str(required=True)
    rating = fields.Str(required=True)

class MovieUpdateSchema(Schema):
    title = fields.Str()
    director = fields.Str()
    year = fields.Int()
    genres = fields.Str()
    runtime = fields.Str()
    original_language = fields.Str()
    rating = fields.Str()

class MultipleMoviesSchema(Schema):
    movies = fields.List(fields.Nested(MovieSchema), required=True)
    error_messages = fields.List(fields.Str(), required=False)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
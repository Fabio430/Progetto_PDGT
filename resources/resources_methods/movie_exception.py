class MovieExceptions:
    class MovieAlreadyExistsError(Exception):
        # Raised when a movie with the same title, director, and year already exists
        def __init__(self, message="This movie already exists"):
            self.message = message
            super().__init__(self.message)

    class InvalidYearError(Exception):
        # Raised when the movie year is invalid
        def __init__(self, message="The year is not correct"):
            self.message = message
            super().__init__(self.message)

    class InvalidDirectorInputError(Exception):
        # Raised when the director's name format is invalid
        def __init__(self, message="The format of the director's name is not correct"):
            self.message = message
            super().__init__(self.message)

    class InvalidLanguageInputError(Exception):
        # Raised when the original language format is invalid
        def __init__(self, message="The format of the original language is not valid"):
            self.message = message
            super().__init__(self.message)

    class InvalidTitleInputError(Exception):
        # Raised when the movie title format is invalid
        def __init__(self, message="The format of the title is not valid"):
            self.message = message
            super().__init__(self.message)

    class InvalidGenreInputError(Exception):
        # Raised when the genre format is invalid
        def __init__(self, message="The format of the genres is not valid"):
            self.message = message
            super().__init__(self.message)

    class InvalidRatingInputError(Exception):
        # Raised when the rating format is invalid
        def __init__(self, message="The format of the rating is not valid"):
            self.message = message
            super().__init__(self.message)

    class InvalidRuntimeInputError(Exception):
        # Raised when the runtime format is invalid
        def __init__(self, message="The format of the runtime is not valid"):
            self.message = message
            super().__init__(self.message)

    class DatabaseError(Exception):
        # Raised when there is an error interacting with the database
        def __init__(self, message="An error occurred interacting with the database"):
            self.message = message
            super().__init__(self.message)
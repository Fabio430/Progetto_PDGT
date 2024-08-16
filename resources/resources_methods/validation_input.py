import re

class ValidationFunctions():
    # Function to capitalize strings in a dictionary
    @staticmethod
    def title_dict(d):
        title_dict = {}
        capitalized_words = []
        for key, value in d.items():
            if isinstance(value, str):
                if "'" in value:
                    words = value.split(" ")
                    for word in words:
                        capitalized_words.append(word.capitalize())
                    value = " ".join(capitalized_words)
                    title_dict[key] = value
                else:
                    title_dict[key] = value.title()
            else:
                title_dict[key] = value
        return title_dict
    
    @staticmethod
    def validate_director_input(input_string):
        pattern = r"^(?!\s)(?!.*\s{2,})(?!.*[^\w\s\-'!,.:&?()\[\]])[^\s@][\w\s\-',.!&:?()\[\]]*[^\s@]$"
        return re.match(pattern, input_string) is not None
    
    @staticmethod
    def validate_original_language_input(input_string):
        pattern = r"^[A-Za-z]+(?:[\s-][A-Za-z]+)*$"
        return re.match(pattern, input_string) is not None
    
    @staticmethod
    def validate_title_input(input_string):
        pattern = r"^(?!\s)(?!.*\s{2,})(?!.*[^\w\s\-'!,.:&?()\[\]])[^\s@][\w\s\-',.!&:?()\[\]]*[^\s@]$"
        return re.match(pattern, input_string) is not None

    @staticmethod
    def genre_input_string(input_string):
        pattern = r"^[A-Za-z]+(?:-[A-Za-z]+)?(?:, [A-Za-z]+(?:-[A-Za-z]+)?)*$"
        return re.match(pattern, input_string) is not None
    
    @staticmethod
    def is_unique_word_list(input_string):
        words = input_string.split(',')
        return len(words) == len(set(words))

    @staticmethod
    def validate_genre_input(input_string):
        return ValidationFunctions.genre_input_string(input_string) and ValidationFunctions.is_unique_word_list(input_string)

    @staticmethod
    def validate_rating_input(input_str):
        pattern = r"^[1-5]/5$"
        return re.match(pattern, input_str) is not None

    @staticmethod
    def validate_runtime_input(input_str):
        pattern = r"^\d+\sMins$"
        return re.match(pattern, input_str) is not None
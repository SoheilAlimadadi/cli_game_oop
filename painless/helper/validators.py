from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation
)

from .exceptions import (
    PasswordUpperCaseError,
    PasswordDigitError,
    PasswordLengthError,
    PasswordLetterError,
    PasswordLowerCaseError,
    PasswordSignError,
    UsernameLengthError,
    UsernameStartDigitError
)


class UsernameValidator:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not self.username_length_validator(value):
            raise UsernameLengthError

        if not self.username_starts_alpha(value):
            raise UsernameStartDigitError

        self._username = value

    def username_length_validator(self, value):
        is_valid = False
        if len(value) > 3:
            is_valid = True

        return is_valid

    def username_starts_alpha(self, value):
        is_valid = False
        if value[0].isalpha():
            is_valid = True

        return is_valid


class PasswordValidator:

    def __init__(self, password):
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not self.password_length(value):
            raise PasswordLengthError
        if not self.password_alpha(value):
            raise PasswordLetterError
        if not self.password_uppercase(value):
            raise PasswordUpperCaseError
        if not self.password_lowercase(value):
            raise PasswordLowerCaseError
        if not self.password_digit(value):
            raise PasswordDigitError
        if not self.password_sign(value):
            raise PasswordSignError

        self._password = value

    def password_length(self, password):
        is_valid = False
        if len(password) > 8:
            is_valid = True

        return is_valid

    def password_alpha(self, password):
        is_valid = False
        if any(map(lambda letter: letter in ascii_letters, password)):
            is_valid = True
        
        return is_valid

    def password_uppercase(self, password):
        is_valid = False
        if any([letter in ascii_uppercase for letter in password]):
            is_valid = True
        
        return is_valid

    def password_lowercase(self, password):
        is_valid = False
        if any(map(lambda letter: letter in ascii_lowercase, password)):
            is_valid = True
        
        return is_valid

    def password_digit(self, password):
        is_valid = False
        if any(map(lambda letter: letter in digits, password)):
            is_valid = True
        
        return is_valid

    def password_sign(self, password):
        is_valid = False
        if any(map(lambda letter: letter in punctuation, password)):
            is_valid = True
        
        return is_valid

from entities.user import User
import re
import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already in use")
        if not re.match("(^.[a-z]{2,})+$", username):
            raise UserInputError("Username too short or includes a character not allowed")
        if not re.match("(?=^.[a-zA-Z]*[^a-zA-Z]+[a-zA-Z]*)(?=^.{8,})", password):
            raise UserInputError("Password too short or only includes alphabets")
        #Salasanan on oltava pituudeltaan vähintään 8 merkkiä ja se ei saa koostua pelkästään kirjaimista.

from sqlalchemy import sql

from painless.helper.validators import (
    UsernameValidator,
    PasswordValidator
)
from database.models import UserModel
from painless.helper.exceptions import (
    PasswordUpperCaseError,
    PasswordDigitError,
    PasswordLengthError,
    PasswordLetterError,
    PasswordLowerCaseError,
    PasswordSignError,
    UsernameLengthError,
    UsernameStartDigitError
)
from painless.helper.settings import GameState

from painless.helper.exceptions import (
    PasswordUpperCaseError,
    PasswordDigitError,
    PasswordLengthError,
    PasswordLetterError,
    PasswordLowerCaseError,
    PasswordSignError,
    UsernameLengthError,
    UsernameStartDigitError
)
class User(UserModel):
    
    @classmethod
    def create(cls, username, password):
        user = cls(
            username=username,
            password=password
        )
        cls.database.session.add(user)
        cls.database.session.commit()

    @classmethod
    def check_username(cls, username):
        stmt = sql.select(cls) \
                    .where(cls.username == username)
        user = cls.database.session.execute(stmt).one_or_none()
        return user

    @classmethod
    def check_password(cls, username, password):
        password_correct = False
        name = cls.check_username(username)
        if name:
            stmt = sql.select(cls) \
                        .filter(cls.username == username) \
                            .where(cls.password == password)
            if cls.database.session.execute(stmt).one_or_none():
                password_correct = True
        return password_correct

    @classmethod
    def update_username(cls, old_username, new_username):
        stmt = sql.update(cls) \
                    .where(cls.username == old_username) \
                        .values(username=new_username)
        cls.database.session.execute(stmt)
        cls.database.session.commit()

    @classmethod
    def update_password(cls, username, old_password, new_password):
        stmt = sql.update(cls) \
                    .filter(cls.username == username) \
                    .where(cls.password == old_password) \
                        .values(password=new_password)
        cls.database.session.execute(stmt)
        cls.database.session.commit()

    @classmethod
    def get_info(cls):
        stmt = sql.select(cls.username, cls.won, cls.loss, cls.win_ratio)
        info = cls.database.session.execute(stmt).fetchall()
        return info

    @classmethod
    def update_ratio(cls, username, result):
        stmt = sql.select(cls.username, cls.won, cls.loss) \
                    .where(cls.username == username)
        username, won, loss = cls.database.session.execute(stmt).one()
        if result == GameState.WIN:
            won = won + 1
        elif result == GameState.LOSE:
            loss = loss + 1
        win_ratio = (won / (won + loss)) * 100

        stmt = sql.update(cls) \
                    .where(cls.username == username) \
                        .values(won=won, loss=loss, win_ratio=win_ratio)
        cls.database.session.execute(stmt)
        cls.database.session.commit()

    @classmethod
    def delete(cls, username):
        stmt = sql.delete(cls) \
                    .where(cls.username == username)
        cls.database.session.execute(stmt)
        cls.database.session.commit()


class Username:
    @staticmethod
    def check(username):
        is_valid = False
        try:
            username = UsernameValidator(username)
        except UsernameLengthError as e:
            print(e)
        except UsernameStartDigitError as e:
            print(e)
        else:
            is_valid = True

        return is_valid


class Password:
    @staticmethod
    def check(password):
        is_valid = False
        try:
            password = PasswordValidator(password)
        except PasswordLengthError as e:
            print(e)
        except PasswordLetterError as e:
            print(e)
        except PasswordUpperCaseError as e:
            print(e)
        except PasswordLowerCaseError as e:
            print(e)
        except PasswordDigitError as e:
            print(e)
        except PasswordSignError as e:
            print(e)
        else:
            is_valid = True
        
        return is_valid

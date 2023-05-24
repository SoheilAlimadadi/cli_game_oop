from enum import StrEnum

from .settings import HomepageButtons as HB
from .settings import MenuButtons as MB


class PasswordErrorMessages(StrEnum):
    '''Error messages regarding password'''
    PASSWORD_GENERIC_ERROR: str = "Password is not acceptable"
    PASSWORD_LENGTH_ERROR: str = "Password must be atleast 8 characters"
    PASSWORD_LETTER_ERROR: str = "Password must have atleast 2 letters"
    PASSWORD_SIGN_ERROR: str = "Password must have atleast 1 sign character"
    PASSWORD_DIGIT_ERROR: str = "Password must have atleast 1 digit"
    PASSWORD_UPPER_ERROR: str = "Password must have atleast 1 uppercase letter"
    PASSWORD_LOWER_ERROR: str = "Password must have atleast 1 lowercase letter"


class UsernameErrorMessages(StrEnum):
    '''Error messages regarding username'''
    USERNAME_LENGTH_ERROR: str = "Username must be atleast 4 characters"
    USERNAME_AlPHA: str = "Username must start with an alphabet character"


class HomepageMessages(StrEnum):
    '''Error messages used in homepage'''
    LOGIN_TEXT: str = f"Enter '{HB.LOGIN_BUTTON.upper()}' to login"
    REGISTER_TEXT: str = f"Enter '{HB.REGISTER_BUTTON.upper()}' to register"
    QUIT_TEXT: str = f"Enter '{HB.QUIT_BUTTON.upper()}' to quit"
    GET_USERNAME_TEXT: str = "Username: "
    GET_PASSWORD_TEXT: str = "Password: "
    GET_REPEAT_PASSWORD: str = "Repeat password: "
    USERNAME_NOT_FOUND: str = "'{}' is not registered"
    PWS_DONT_MATCH: str = "Passwords do not match, try again!"
    QUIT_LOGIN: str = "Enter 'B' to go back to homepage"
    LOGIN_UNSUCCESSFUL: str = "Username and password do not match"
    USER_EXISTS = "'{}' already exists, try another username"


class DatabaseVariables(StrEnum):
    '''Variables used in Database class'''
    DATABASE_NAME: str = 'database.json'
    PLAYERS: str = 'players'
    WIN_RATIO: str = 'win ratio'
    GAMES_WON: str = 'won'
    GAMES_LOST: str = 'lost'
    PASSWORD: str = 'password'
    SALT: str = 'salt'
    WRITE: str = 'w'
    READ: str = 'r'


class MenuMessages(StrEnum):
    '''Messages used in Menu class'''
    WELCOME_MESSAGE: str = "Welcome {}!"
    GAME_DIFFS_TEXT: str = (
        f"Easy: {MB.EASY_DIFF}, Normal: {MB.NORMAL_DIFF}, Hard: {MB.HARD_DIFF}"
    )
    START_GAME_TEXT: str = "Enter The desired difficulty to start the game"
    LEADERBOARD_TEXT: str = (
        f"Enter '{MB.LEADERBOARD.upper()}' to see the leaderboard")
    LOGOUT_TEXT: str = f"Enter '{MB.LOGOUT.upper()}' to logout"


class AxisErrorMessages(StrEnum):
    '''Error messages regarding Axis'''
    AXIS_TYPE_ERROR: str = "Non-integer value was assinged to {}"
    VALUE_NEGATIVE: str = "Negative value was assigned to {}"


class GameMessages(StrEnum):
    '''Messages used while in game'''
    HEALTH: str = "Health: {}"
    ALERT: str = "ALERT: {} is suspicious and might move towards you!"
    MOVEMENTS: str = "Enter {} to move"
    BACK: str = "Enter {} to go back to menu"
    MOVE: str = "Move: "
    SHOOT: str = "Enter {} to shoot"


class GameResultMessages(StrEnum):
    '''Game result messages'''
    WIN: str = '''
██╗░░░██╗░█████╗░██╗░░░██╗ ░██╗░░░░░░░██╗░█████╗░███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║ ░██║░░██╗░░██║██╔══██╗████╗░██║
░╚████╔╝░██║░░██║██║░░░██║ ░╚██╗████╗██╔╝██║░░██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║ ░░████╔═████║░██║░░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝ ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░ ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝
'''

    LOSE: str = '''
██╗░░░██╗░█████╗░██╗░░░██╗ ██╗░░░░░░█████╗░░██████╗████████╗
╚██╗░██╔╝██╔══██╗██║░░░██║ ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝
░╚████╔╝░██║░░██║██║░░░██║ ██║░░░░░██║░░██║╚█████╗░░░░██║░░░
░░╚██╔╝░░██║░░██║██║░░░██║ ██║░░░░░██║░░██║░╚═══██╗░░░██║░░░
░░░██║░░░╚█████╔╝╚██████╔╝ ███████╗╚█████╔╝██████╔╝░░░██║░░░
░░░╚═╝░░░░╚════╝░░╚═════╝░ ╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░
'''
    AFTER_GAME: str = "Press RETURN to go back to menu"


class LogMessages(StrEnum):
    '''Messages used for logging'''
    PROGRAM_RUN = "Anonymous started the game"
    PROGRAM_EXITED = "Anonymous Exited the game in homepage"
    LOGGED_OUT = "{} Logged out"
    LOGGED_IN = "{} Logged in"
    STARTED_GAME = "{} started the game"
    USERNAME_REGISTER = "{} is attempting to register with a valid username"
    FAILED_USERNAME_REGISTER = (
        "User failed to register with '{}' as username\n")
    REGISTERED = "{} registered"
    RESULT = "{} {} the game"
    EXIT_GAME = "{} came out of the game before finishing the game"
    SHOT_WALL_TYPEERROR = (
        "Player shot at top or bottom wall of the map TypeError")
    SHOT_WALL_INDEXERROR = (
        "Player shot at top or bottom wall of the map IndexError")

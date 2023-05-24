from enum import StrEnum, Enum
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class HomepageButtons(StrEnum):
    LOGIN_BUTTON: str = 'l'
    REGISTER_BUTTON: str = 'r'
    QUIT_BUTTON: str = 'q'
    LOGIN_BACK: str = 'b'


class MenuButtons(StrEnum):
    EASY_DIFF: str = '1'
    NORMAL_DIFF: str = '2'
    HARD_DIFF: str = '3'
    LEADERBOARD: str = 'l'
    LOGOUT: str = 'q'


class LeaderBoardVars(StrEnum):
    NAME: str = 'Name'
    WON: str = 'Games won'
    LOST: str = 'Games lost'
    RATIO: str = 'Win ratio'
    NO_USERS: str = "No registered users yet"
    TABLE_STYLE: str = 'grid'
    PRESS_ANY: str = '\n\nEnter any key to go back.'


class ValidGameInputs(StrEnum):
    UP: str = 'up'
    DOWN: str = 'down'
    RIGHT: str = 'right'
    LEFT: str = 'left'
    BACK: str = 'q'


class GameBoardElements(StrEnum):
    MAP_WALLS: str = '⬛'
    MAP_TILES: str = '⬜'


class GameBoardSize(Enum):
    MAP_WIDTH: int = 17
    MAP_HEIGHT: int = 17


class GameMechanicElemenets(StrEnum):
    X: str = 'x'
    Y: str = 'y'


class MonsterSettings(StrEnum):
    MONSTER_STR: str = 'monster'
    MONSTER: str = '🐉'
    DRAGON_NUM: str = '3'


class PlayerSettings(StrEnum):
    PLAYER_STR: str = 'player'
    PLAYER: str = '😎'
    HEALTH: str = '💜'
    HEALTH_NUM: str = '3'
    SHOTS: str = '🔥'


class ShootValidInputs(StrEnum):
    UP = 'shoot up'
    DOWN = 'shoot down'
    RIGHT = 'shoot right'
    LEFT = 'shoot left'


class PlayerShootSettings(Enum):
    SHOTS_NUM = 3
    UP = 'shoot up'
    DOWN = 'shoot down'
    RIGHT = 'shoot right'
    LEFT = 'shoot left'
    UP_DIR = ((0, -1), (0, -2))
    DOWN_DIR = ((0, 1), (0, 2))
    RIGHT_DIR = ((1, 0), (2, 0))
    LEFT_DIR = ((-1, 0), (-2, 0))


class DungeonDoorSettings(StrEnum):
    DOOR_STR: str = 'dungeon door'
    EMOJI: str = '🟥'


class MovementSettings(Enum):
    UP_INPUT: str = 'up'
    DOWN_INPUT: str = 'down'
    LEFT_INPUT: str = 'left'
    RIGHT_INPUT: str = 'right'
    UP: tuple[int, int] = (0, -1)
    DOWN: tuple[int, int] = (0, 1)
    RIGHT: tuple[int, int] = (1, 0)
    LEFT: tuple[int, int] = (-1, 0)


class GameState(StrEnum):
    ON_GOING: str = 'on going'
    WIN: str = 'won'
    LOSE: str = 'lost'

LOG_FILES = (
    "logs/auth.log",
    "logs/game.log",
    "logs/root.log"
)

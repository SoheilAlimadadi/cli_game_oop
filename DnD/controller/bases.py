from math import dist
from random import (
    randint,
    choice
)

from .mechanics import Movement
from painless.helper.settings import (
    GameBoardSize as GBS,
    PlayerSettings as PS,
    MonsterSettings as MS,
    PlayerShootSettings as PSS,
    GameBoardElements as GBE
)


class BasePlayer(Movement):
    """The base class for player"""
    def __init__(self, game_board: list[list[str]]) -> None:
        self.emoji: str = PS.PLAYER
        self.string: str = PS.PLAYER_STR
        self.health: list[str] = [PS.HEALTH for _ in range(int(PS.HEALTH_NUM))]
        self.shots: list[str] = [
            PS.SHOTS for _ in range(PSS.SHOTS_NUM.value)
        ]
        self.game_board = game_board
        self.X = GBS.MAP_WIDTH.value // 2
        self.Y = GBS.MAP_HEIGHT.value - 2
        self.coord: tuple[int, int] = (self.Y, self.X)

    def __str__(self) -> str:
        return self.string


class BaseMonster(Movement):
    """Base monster class"""
    def __init__(self, game_board: list[list[str]]) -> None:
        self.string: str = MS.MONSTER_STR
        self.emoji: str = MS.MONSTER
        self.game_board = game_board
        x, y = self.random_xy()
        self.X = x
        self.Y = y
        self.coord = (self.Y, self.X)

    def random_xy(self) -> tuple[int, int]:
        """ """
        random_coord_valid = False
        while not random_coord_valid:
            x = randint(2, GBS.MAP_WIDTH.value - 2)
            y = randint(2, GBS.MAP_HEIGHT.value - (GBS.MAP_HEIGHT.value // 3))
            if self.game_board[y][x] == GBE.MAP_TILES:
                random_coord_valid = True
                coord = (x, y)

        return coord

    def move_if_smell(self, player_coord: tuple[int, int]) -> None:
        """

        Parameters
        ----------
        player_coord: tuple[int, int] : cooordinate of the player


        Returns None
        -------

        """
        if dist(self.coord, player_coord) < 5:
            direction = choice(list(self.movements.keys()))
            self.move(direction)

    def __str__(self) -> str:
        return self.string

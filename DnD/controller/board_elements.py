from random import randint

from .bases import (
    BasePlayer,
    BaseMonster
)
from painless.helper.settings import (
    DungeonDoorSettings as DDS,
    GameBoardSize as GBS,
    GameBoardElements as GBE,
    PlayerShootSettings as PSS
)


class Player(BasePlayer):
    """ """

    shoot_directions = {
        PSS.UP.value: PSS.UP_DIR.value,
        PSS.DOWN.value: PSS.DOWN_DIR.value,
        PSS.RIGHT.value: PSS.RIGHT_DIR.value,
        PSS.LEFT.value: PSS.LEFT_DIR.value,
    }

    def shoot(self, user_input: str) -> list[tuple[int, int]]:
        """

        Parameters
        ----------
        user_input: str : user input


        Returns list[tuple[int, int]]: a list of coordinate of the shots fired
        -------

        """
        shots = list()
        shot_direction = self.shoot_directions[user_input]
        for shot in shot_direction:
            x, y = self.coord
            x_shot, y_shot = shot

            new_x = x + y_shot
            new_y = y + x_shot
            shot_coord = (new_x, new_y)

            shots.append(shot_coord)
        return shots


class Door:
    """
    a class with dungeon door info
    and generates a semi-random location for it
    """

    def __init__(self, game_board: list[list[str]]) -> None:
        self.emoji: str = DDS.EMOJI
        self.string: str = DDS.DOOR_STR
        self.game_board = game_board
        self.coord = self.random_coord()

    def random_coord(self) -> tuple[int, int]:
        """
        Generates a semi-random location for the dungeon door

        returns Coordinate: the dungeon door coord
        """
        coord_valid = False
        while not coord_valid:
            x = randint(1, GBS.MAP_WIDTH.value - 2)
            y = randint(
                1, GBS.MAP_HEIGHT.value - (GBS.MAP_HEIGHT.value // 3 + 2)
            )
            if self.game_board[y][x] == GBE.MAP_TILES:
                coord = (y, x)
                coord_valid = True

        return coord

    def __str__(self) -> str:
        return self.string


class Dragon(BaseMonster):
    """
    Dragon is a kind of monster
    """
    pass

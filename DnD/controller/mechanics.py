from logging import getLogger
from math import dist

from painless.utils.funcs import clean
from painless.helper.messages import GameResultMessages as GRM
from painless.helper.settings import (
    GameState as GS,
    MovementSettings as MS,
    GameBoardElements as GBE
)
from painless.helper.exceptions import (
    XAxisTypeError,
    YAxisTypeError,
    XAxisNegativeError,
    YAxisNegativeError
)

game_logger = getLogger('game')


class Game:
    """Mechanics of the game are implemented here"""
    def __init__(self, game_board: list[list[str]]):
        self.game_board: list[list[str]] = game_board

    def update_game_state(
        self,
        player_coord: tuple[int, int],
        door_coord: tuple[int, int],
        hp: list[str],
        monsters: list,
        shots: list[tuple[int, int]]
    ) -> tuple[str, list[tuple[int, int]]]:
        """Checks whether the game is on going, won or loss on each loop
        if player is next to the dragon, loses on of his/her healths

        Parameters
        ----------
        player_coord: tuple[int, int] : coordinate of player

        door_coord: tuple[int, int] : cooordinate of the door

        hp: list[str] : a list of healths

        monsters: list : a list of monster objects

        shots: list[tuple[int, int] : a list of shot coordinates


        Returns tuple[str, tuple[int, int]]: state of the game and and and
                                            a list of monster objects
        -------

        """
        game_state: str = GS.ON_GOING
        for monster in monsters:
            if dist(player_coord, monster.coord) <= 1:
                hp.pop()
            if player_coord == monster.coord or not hp:
                game_state: str = GS.LOSE
            for shot in shots:
                if shot == monster.coord:
                    monsters.remove(monster)
        if player_coord == door_coord:
            game_state: str = GS.WIN

        return game_state, monsters

    def result(self, game_state: str) -> str:
        """Prints the result of the game and returns the game state

        Parameters
        ----------
        game_state: str : state of the game


        Returns str: state of the game
        -------

        """
        clean()
        if game_state is GS.LOSE:
            print(GRM.LOSE)
        else:
            print(GRM.WIN)

        return game_state


class XYValidator:
    '''
    Validates the X and Y axis
    '''
    def is_x_int(x: int, _) -> None:
        '''Raises XAxisTypeError if x is not int'''
        if not isinstance(x, int):
            raise XAxisTypeError

    def is_x_positive(x: int) -> None:
        '''Raises XAxisNegativeError if x is a negative number'''
        if not x >= 0:
            raise XAxisNegativeError

    def is_y_int(y: int, _) -> None:
        '''Raises YAxisTypeError if x is not int'''
        if not isinstance(y, int):
            raise YAxisTypeError

    def is_y_positive(y: int) -> None:
        '''Raises YAxisNegativeError if y is a negative number'''
        if not y >= 0:
            raise YAxisNegativeError


class Axis(XYValidator):
    '''
    Validates and sets the Axis
    '''
    def __init__(self, coord: tuple[int, int]) -> None:
        x, y = coord
        self.X = x
        self.Y = y
        self.coord = (self.Y, self.X)

    @property
    def X(self) -> int:
        return self._X

    @X.setter
    def X(self, value: int) -> None:
        try:
            self.is_x_int(value)
            self.is_x_positive(value)
        except XAxisTypeError as e:
            game_logger.info(e)
        except XAxisNegativeError as e:
            game_logger.info(e)

        self._X = value

    @property
    def Y(self) -> int:
        return self._Y

    @Y.setter
    def Y(self, value: int) -> None:
        try:
            self.is_y_int(value)
            self.is_y_positive(value)
        except YAxisTypeError as e:
            game_logger.info(e)
        except YAxisNegativeError as e:
            game_logger.info(e)

        self._Y = value


class Movement(Axis):
    """Extends the Axis class with movement ability"""

    movements: dict[str, tuple[int, int]] = {
        MS.UP_INPUT.value: MS.UP.value,
        MS.DOWN_INPUT.value: MS.DOWN.value,
        MS.LEFT_INPUT.value: MS.LEFT.value,
        MS.RIGHT_INPUT.value: MS.RIGHT.value
    }

    def __init__(
        self,
        coord: tuple[int, int],
        game_board: list[list[str]]
    ) -> None:
        super().__init__(coord)
        self.game_board = game_board

    def move(self, user_input: str) -> None:
        """

        Parameters
        ----------
        user_input: str : user input


        Returns None
        -------

        """
        x, y = self.coord
        if user_input:
            x_move, y_move = self.movements[user_input]
            new_x = x + y_move
            new_y = y + x_move
            self.coord = (new_x, new_y)

    def check_wall_collision(
        self,
        coord: tuple[int, int],
        gameboard: list[list[str]]
    ) -> bool:
        """Checks whether the object has colided with wall

        Parameters
        ----------
        coord: tuple[int, int]: coordinate of object

        gameboard: list[list[str]] : game board


        Returns bool: True if valid else False
        -------

        """
        valid_pos: bool = False
        if coord:
            x, y = coord
            if not gameboard[x][y] == GBE.MAP_WALLS:
                valid_pos = True

        return valid_pos

    @property
    def coord(self) -> tuple[int, int]:
        return self._coord

    @coord.setter
    def coord(self, value: tuple[int, int]) -> None:
        if self.check_wall_collision(value, self.game_board):
            self._coord = value

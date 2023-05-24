from logging import getLogger

from painless.helper.settings import (
    GameBoardElements as GBE,
    GameBoardSize as GBS
)
from painless.helper.messages import LogMessages as LM


game_logger = getLogger('game')


class GameBoard:
    """Class for the gameboard of the game"""

    def __init__(self) -> None:
        self.row_len: str = GBS.MAP_WIDTH.value
        self.col_len: str = GBS.MAP_HEIGHT.value
        self.walls: str = GBE.MAP_WALLS
        self.tiles: str = GBE.MAP_TILES

    def make_board(self) -> list[list[str]]:
        """Creates the gameboard

           returns list[list[str]]: game board
        """
        game_map = [
            self.walls * self.row_len if col == 0 or col == (self.col_len - 1)
            else [self.walls if row == 0 or row == (self.row_len - 1)
                  else self.tiles for row in range(self.row_len)]
            for col in range(self.col_len)]

        for col in range(2, self.col_len - 2, 3):
            if col % 2 == 0:
                for row in range(2, self.row_len - 1):
                    game_map[col][row] = self.walls

            else:
                for row in range(1, self.row_len - 2):
                    game_map[col][row] = self.walls

        return game_map

    @staticmethod
    def place_on_board(
        board: list[list[str]],
        coord: tuple[int, int],
        obj: str
    ) -> tuple[int, int]:
        """Draws objects onto the gameboard

        Parameters
        ----------
        board: list[list[str]] : game board

        coord: tuple[int, int] : coordinate of the object

        obj: str : the object


        Returns tuple[int, int]: coord of the object
        -------

        """
        try:
            xpos, ypos = coord
            board[xpos][ypos] = obj
        except TypeError:
            game_logger.info(LM.SHOT_WALL_TYPEERROR)
        except IndexError:
            game_logger.info(LM.SHOT_WALL_INDEXERROR)

        return coord

    @staticmethod
    def delete(board: list[list[str]], coord: tuple[int, int]) -> None:
        """Deletes objects from the gameboard

        Parameters
        ----------
        board: list[list[str]]: game board

        coord: tuple[int, int] : coordinate of the object

        Returns None
        -------

        """
        xpos, ypos = coord
        board[xpos][ypos] = GBE.MAP_TILES

    @staticmethod
    def draw_game_board(board: list[list[str]]) -> None:
        """Draws the gameboard

        Parameters
        ----------
        board: list[list[str]] : game board


        Returns None
        -------

        """
        for row in board:
            print(''.join(row))

from typing import (
    Optional,
    Callable
)
from logging import getLogger
from time import sleep

from tabulate import tabulate

from DnD.controller.user import (
    User,
    Username,
    Password
)
from DnD.controller.game_board import GameBoard
from DnD.controller.mechanics import Game
from DnD.controller.board_elements import (
    Player,
    Dragon,
    Door
)
from painless.helper.messages import (
    LogMessages as LG,
    MenuMessages as MM,
    GameMessages as GM,
    HomepageMessages as HM,
    GameResultMessages as GRM
)
from painless.helper.settings import (
    GameState as GS,
    MenuButtons as MB,
    PlayerSettings as PS,
    HomepageButtons as HB,
    LeaderBoardVars as LBV,
    ValidGameInputs as VGI,
    ShootValidInputs as SVI
)
from painless.utils.funcs import (
    clean,
    wait_clean,
    print_logo
)

root_logger = getLogger('root')
game_logger = getLogger('game')
auth_logger = getLogger('auth')


class HomePageView:
    """
    The homepage of the game
    user can register, login and quit here
    """
    texts: list[str] = [HM.LOGIN_TEXT, HM.REGISTER_TEXT, HM.QUIT_TEXT]
    buttons: list[str] = [HB.LOGIN_BUTTON, HB.REGISTER_BUTTON, HB.QUIT_BUTTON]

    @classmethod
    def home_page(cls) -> tuple[str, bool]:
        """Creates the homepage"""
        quit_game: bool = False
        home_page: bool = True
        username: Optional[str] = None
        while home_page:
            clean()
            print_logo()
            for text in cls.texts:
                print(text)

            user_input = input().lower().strip()
            clean()

            if user_input == HB.QUIT_BUTTON:
                quit_game, home_page = True, False
            if user_input == HB.REGISTER_BUTTON:
                cls.register_user()
            if user_input == HB.LOGIN_BUTTON:
                username, logged_in = cls.login_user()
                if not logged_in:
                    continue

                home_page = False

        return username, quit_game

    @staticmethod
    def register_user() -> None:
        """Registers the user"""
        username_valid: bool = False
        while not username_valid:
            print_logo()
            username = input(HM.GET_USERNAME_TEXT)
            if not User.check_username(username):
                username_valid = Username.check(username)
                if not username_valid:
                    sleep(2)
            else:
                print(HM.USER_EXISTS.format(username))
                sleep(2)
            clean()

        password, repeat_password = False, True
        while not password == repeat_password:
            if password is False:
                print_logo()
            password = input(HM.GET_PASSWORD_TEXT)
            password_valid = Password.check(password)
            if not password_valid:
                continue
            repeat_password = input(HM.GET_REPEAT_PASSWORD)
            if not password == repeat_password:
                print(HM.PWS_DONT_MATCH)
                sleep(2)

            clean()

        User.create(username, password)

    @staticmethod
    def login_user() -> tuple[str, bool]:
        """Logs in the user

        returns tuple[str, bool]: username and whether user is logged in or not
        """
        logged_in: bool = False
        while not logged_in:
            clean()
            print_logo()
            print(HM.QUIT_LOGIN)
            username = input(HM.GET_USERNAME_TEXT)
            if username.lower() == HB.LOGIN_BACK:
                break
            if not User.check_username(username):
                print(HM.USERNAME_NOT_FOUND.format(username))
                wait_clean()
                continue
            password = input(HM.GET_PASSWORD_TEXT)
            if password.lower() == HB.LOGIN_BACK:
                break
            clean()

            is_valid: bool = User.check_password(username, password)
            if is_valid:
                auth_logger.info(LG.LOGGED_IN.format(username))
                logged_in = True
            else:
                print_logo()
                print(HM.LOGIN_UNSUCCESSFUL)
                sleep(2)

        return username, logged_in


class MenuView:
    """
    Menu of the game
    Start game, log out and show leaderboard are the options
    """
    game_diffs: list[str] = [
            MB.EASY_DIFF,
            MB.NORMAL_DIFF,
            MB.HARD_DIFF
        ]
    messages: list[str] = [
            MM.GAME_DIFFS_TEXT,
            MM.START_GAME_TEXT,
            MM.LEADERBOARD_TEXT,
            MM.LOGOUT_TEXT
        ]
    @classmethod
    def make_menu(cls, username=None) -> tuple[bool, bool, int]:
        '''Creates the menu

           return tuple[bool, bool]: is user logged-out, start game or not and
            difficulty of the game
        '''
        menu: bool = True
        logout: bool = False
        start_game: bool = False
        game_diff = 0

        while menu:
            clean()
            print_logo()
            print(MM.WELCOME_MESSAGE.format(username))
            for message in cls.messages:
                print(message)

            user_input = input().lower().strip()
            clean()

            if user_input == MB.LOGOUT:
                menu, logout = False, True
            if user_input in cls.game_diffs:
                game_diff = int(user_input)
                start_game = True
                menu = False
            if user_input == MB.LEADERBOARD:
                leaderboard = LeaderboardView()
                leaderboard.show_leaderboard()

        return logout, start_game, game_diff


class LeaderboardView:
    """Leaderboard showing games won, games lost and win ratio of each user"""
    name: str = LBV.NAME
    won: str = LBV.WON
    lost: str = LBV.LOST
    ratio: str = LBV.RATIO
    no_registers: str = LBV.NO_USERS
    style: str = LBV.TABLE_STYLE
    any_key: str = LBV.PRESS_ANY

    @classmethod
    def show_leaderboard(cls) -> None:
        """Prints a table in the terminal containing the game's leaderboard"""

        players_stats = User.get_info()
        sorted_players = sorted(
            players_stats, key=lambda player: player[3]
        )[::-1]
        sorted_players = [
            (player[0:3]) + (f"{player[3]:.2f} %",) for player in sorted_players
        ]
        if not len(sorted_players):
            print(cls.no_registers)
        else:
            headers = [cls.name, cls.won, cls.lost, cls.ratio]
            rows = sorted_players
            print(tabulate(rows, headers, tablefmt=cls.style))
        print(cls.any_key)
        input()
        clean()


class GameView:

    @classmethod
    def game(cls, username: str, diff: int) -> Callable:
        """setting up the objects needed in the game
        running the main loop of the game

        Parameters
        ----------
        username: str : username

        diff: int : game difficulty


        Returns Callable: run_pregame method is called after run_game
        -------

        """
        board = GameBoard()
        game_board = board.make_board()
        game = Game(game_board)
        player = Player(game_board)
        door = Door(game_board)
        monsters = [Dragon(game_board) for _ in range(diff)]
        valid_inputs: list[str] = [value for value in VGI.__members__.values()]
        valid_shot_inputs: list[str] = [
            value for value in SVI.__members__.values()
        ]
        all_valid_inputs = valid_shot_inputs + valid_inputs
        game_end, result = False, None

        while not game_end:
            shots = list()
            board_elements = [player, door, *monsters]
            for element in board_elements:
                GameBoard.place_on_board(
                    game_board, element.coord, element.emoji
                )
            GameBoard.draw_game_board(game_board)
            cls.print_info(valid_shot_inputs, valid_inputs, player.health)
            user_input = input(GM.MOVE)
            clean()

            if user_input not in all_valid_inputs:
                continue
            if user_input == VGI.BACK:
                game_logger.info(LG.EXIT_GAME.format(username))
                break

            for element in board_elements:
                GameBoard.delete(game_board, element.coord)

            if user_input in valid_shot_inputs:
                shots = player.shoot(user_input)
                for shot in shots:
                    GameBoard.place_on_board(game_board, shot, PS.SHOTS)
            else:
                player.move(user_input)

            for monster in monsters:
                monster.move_if_smell(player.coord)

            game_state, monsters = game.update_game_state(
                player.coord,
                door.coord,
                player.health,
                monsters,
                shots
            )
            if game_state is not GS.ON_GOING:
                result = game.result(game_state)
                game_logger.info(LG.RESULT.format(username, result))
                user_input: str = input(GRM.AFTER_GAME)
                clean()
                game_end = True

        if result:
            User.update_ratio(username, result)

        return username

    @staticmethod
    def print_info(
        valid_shoot_inputs: list[str],
        valid_inputs: list[str],
        hp: list[str]
    ) -> None:
        """Prints info while the game is running

        Parameters
        ----------
        valid_shoot_inputs: list[str] : valid inputs for shooting

        valid_inputs: list[str] : valid inputs for movements

        hp: list[str] : a list of healths


        Returns None
        -------

        """
        print(GM.HEALTH.format(" ".join(hp)))
        print(GM.MOVEMENTS.format(" ,".join(valid_inputs[:-1])))
        print(GM.SHOOT.format(" ,".join(valid_shoot_inputs)))
        print(GM.BACK.format(VGI.BACK))

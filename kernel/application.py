import logging.config
from logging import getLogger
from typing import Callable

from DnD.view.view import (
    HomePageView,
    MenuView,
    GameView
)
from painless.helper.messages import LogMessages as LG
from painless.helper.settings import BASE_DIR, LOG_FILES
from painless.utils.funcs import create_directories


logging.config.fileConfig(
    fname='config/logging.toml',
    disable_existing_loggers=False
)
root_logger = getLogger('root')
game_logger = getLogger('game')


def run_pregame(username: str = None) -> Callable:
    """runs the homepage and menu

    Parameters
    ----------
    username str: username
            (Default value = None)

    Returns Callable: run_game method is called after this method
    -------

    """
    create_directories(BASE_DIR, LOG_FILES)
    root_logger.info(LG.PROGRAM_RUN)
    start_game: bool = False
    while not start_game:
        if not username:
            username, quit_game = HomePageView.home_page()
            if quit_game:
                root_logger.info(LG.PROGRAM_EXITED)
                exit()
        root_logger.info(LG.LOGGED_IN.format(username))
        logged_out, start_game, diff = MenuView.make_menu(username)
        if logged_out:
            root_logger.info(LG.LOGGED_OUT.format(username))
            username = None
            continue

    root_logger.info(LG.STARTED_GAME.format(username))

    return run_game(username, diff)


def run_game(username, diff):
    username = GameView.game(username, diff)
    return run_pregame(username)

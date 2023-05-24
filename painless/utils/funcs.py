import os
from time import sleep


def create_directories(base_dir: str, directories: list[tuple[str]]):
    """
    Creates a series of directories based on the input parameters.

    Args:
    - base_dir (str): The base directory in which the subdirectories will be created.
    - directories (list of tuples): A list of tuples where each tuple represents a subdirectory to create. 
      The first element of each tuple is the name of the subdirectory, and the rest of the elements (if any) 
      represent subdirectories within the previous directory.

    Example:
    base_dir = '/path/to/base'
    directories = [('logs',), ('logs', 'auth'), ('logs', 'core')]
    create_directories(base_dir, directories)

    This will create the following directories:
    - /path/to/base/logs/auth.log
    - /path/to/base/logs/game.log
    - /path/to/base/logs/root.log
    """
    for directory in directories:
        path = os.path.join(base_dir, directory)
        if not os.path.exists(path):
            os.makedirs(path)

def clean() -> None:
    '''Clear terminal'''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def wait_clean() -> None:
    '''Wait 2 seconds then clear terminal'''
    sleep(2)
    clean()


def print_logo() -> None:
    """Prints game's logo"""
    print(
            """
*********************************
*********** Dungeon *************
************** & ****************
*********** Dragons *************
*********************************
            """)

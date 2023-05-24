# Dungeon and Dragons OOP - v.1.0.0

1: poetry install
2: alembic upgrade head
3: alembic stamp head
4 : python3 run.py (have fun!, you might also need to have special fonts installed for the emojis to work)

## Abstraction

(this project was only tested on macbook)

In this version of DnD once the player runs main.py, player can either login or 
register or quit.
After logging in, player can either start the game with a the preferred
difficulty, see the leaderboard or logout.
Once you start the game:

- the player can get out of the game with 'q'
- Move up, down, right andleft with "up", "down", "right", "left"
- shoot up, down, right and left with 'shoot up', 'shoot down' and so on.

if player gets next to the dragon horizontally or vertically, player will lose
one of the healths shown under the map with '💜'.

if player uses the shoot command, the next 2 cell in that direction will get on
fire and if player shoots at the walls, they get destroyed and if player shoots
at the dragons, dragon will die.
player can even teleport through the map horizontally if he destroys one of the
side walls of the map but he/she can not do the same with top and bottom walls.

## Details of the project

### Sub-packages of the game and modules the modules inside them

- apps
  - home_page: in this module, homepage, register page and login page is placed
  - leaderboard: leader board page
  - make_menu: menu page
- auth
  - auth : password and username exception handling
  - hash: generates salt and hashes the password
  - password: password class that checks password and raises error if not valid
  - username: username class that checks username and raises error if not valid
  - validators: the validators that are used in password and username to check
- database
  - database: everything related to database in in database class
- dungeon_door
  - door: a class for dungeon's door
- enemies
  - base: the base class for monsters of the game
  - dragon: dragons which is one of the monsters
- game_board
  - game_board: creates and draws the game board, can also delete and put objects on the game board
- game_mechanics
  - axis: axis class
  - game: game related logics like determining the result of the game are in game class
  - movement: movement class which inherits from Axis and adds the movement ability to each coordinate
- helper
  - exceptions: custom exceptions of the program
  - messages: messages that are used througout the program are stored here in enums
  - utils: some useful small methods like cleaning the terminal
- logs
  - auth.log - logs related to registery
  - game.log - logs related to game
  - root.log - general logs
  - logs_doc.md - for more info about logs check this file
- players
  - base: the base class for all players
  - player: a generic normal player that has the ability to shoot fire
- settings
  - settings: settings of the game are stored here in enums
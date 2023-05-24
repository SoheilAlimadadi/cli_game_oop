# Documentation of logs used in this game

- root.log (root_logger)

  - logs, when someone runs the program
  - logs, when someone quits the program
  - logs, user login
  - logs, user logout
  - logs, when user starts the game

- auth.log (auth_logger)

  - register logs - password

    - Password must be atleast 8 characters
    - Password must have atleast 2 letters
    - Password must have atleast 1 digit
    - Password must have atleast 1 sign character
    - Password must have atleast 1 uppercase letter
    - Password must have atleast 1 lowercase letter

  - register logs - username

    - User failed to register with 'username' due to UsernameLengthError
    - Username logged in

- game.log (game_logger)
  
  - username came out of the game before finishing the game
  - username lost the game
  - username won the game
  - Non-integer value was assinged to x
  - Non-integer value was assinged to y
  - Negative value was assigned to x
  - Negative value was assigned to y

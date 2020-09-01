import re
import random

_PLAYER = "Player"
_MACHINE = "Machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self):
    # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    if self.check_rows():
      return True
    elif self.check_columns():
      return True
    elif self.check_diagonals():
      return True
    return self.board.count(None) == 0

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell between 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()
    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    replaced = False
    while not replaced:
      i = random.randint(0, 8)
      if self.board[i] is None:
        self.board[i] = _MACHINE_SYMBOL
        replaced = True

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o|
    #   | |
    #   | |
    print(f"""
          {' ' if self.board[0] is None else self.board[0]} | {' ' if self.board[1] is None else self.board[1]} | {' ' if self.board[2] is None else self.board[2]}
          {' ' if self.board[3] is None else self.board[3]} | {' ' if self.board[4] is None else self.board[4]} | {' ' if self.board[5] is None else self.board[5]}
          {' ' if self.board[6] is None else self.board[6]} | {' ' if self.board[7] is None else self.board[7]} | {' ' if self.board[8] is None else self.board[8]}
          """)

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    self.format_board()
    print()

  def check_rows(self):
    first_row_index = 0
    found = False
    while first_row_index < 9 and not found:
      if self.board[first_row_index] == _PLAYER_SYMBOL and self.board[first_row_index + 1] == _PLAYER_SYMBOL and self.board[first_row_index + 2] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        found = True
      elif self.board[first_row_index] == _MACHINE_SYMBOL and self.board[first_row_index + 1] == _MACHINE_SYMBOL and self.board[first_row_index + 2] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        found = True
      first_row_index = first_row_index + 3
    return found

  def check_columns(self):
    first_column_index = 0
    found = False
    while first_column_index < 3 and not found:
      if self.board[first_column_index] == _PLAYER_SYMBOL and self.board[first_column_index + 3] == _PLAYER_SYMBOL and self.board[first_column_index + 6] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        found = True
      elif self.board[first_column_index] == _MACHINE_SYMBOL and self.board[first_column_index + 3] == _MACHINE_SYMBOL and self.board[first_column_index + 6] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        found = True
      first_column_index = first_column_index + 1
    return found

  def check_diagonals(self):
    found = False
    if self.board[0] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL:
      self.winner = _PLAYER
      found = True
    elif self.board[0] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL:
      self.winner = _MACHINE
      found = True
    elif self.board[2] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL:
      self.winner = _PLAYER
      found = True
    elif self.board[2] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL:
      self.winner = _MACHINE
      found = True
    return found

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    print(f"{self.winner} HAS WON!!!")
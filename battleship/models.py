
class Ship():
    def __init__(self, x_axis, y_axis, direction, size, name):
        self.ship_name = name
        self.x_axis = x_axis
        self.y_axis = y_axis


        if direction == 'H' or direction == 'V':
          self.direction = direction
        else:
           raise ValueError("Value must be 'horizontal (H)' or 'vertical (V)'.")
        self.size = size

        self.coordinates = []
        if direction == 'H':
          for i in range(0,size):
              self.coordinates.append({'row': i + self.x_axis, 'col': self.y_axis})

        if direction == 'V':
          for i in range(0,size):
             self.coordinates.append({'row':  self.x_axis, 'col': i + self.y_axis})
    def contains(self, x, y):
          for coords in self.coordinates:
               if str(coords["row"]) == str(x) and str(coords["col"]) == str(y):
                   return True
          return False

    def is_destroyed(self):
            if len(self.coordinates) == 0:
                return True
            else:
                return False





# s --> means contains ship
# x --> mean empty spot
# d --> destroyed part of the ship


class BattleshipGameBoard():
    boardWidth = 10
    boardHeight = 10
    def __init__(self):
        self.shipsonboard = []
        self.game_board = [['x' for x in range(self.boardWidth)] for y in range(self.boardHeight)]

    def add_ship(self, ship):
        self.shipsonboard.append(ship)

    def print_board(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in self.game_board]))



    def fillboard(self):
         print(self.shipsonboard)
         for ship in self.shipsonboard:
             for ship_coodinates in ship.coordinates:
                 print(ship_coodinates)
                 if self.game_board[ship_coodinates["row"]][ship_coodinates["col"]] == 'x':
                      self.game_board[ship_coodinates["row"]][ship_coodinates["col"]] = 's'
                 else:
                      raise IndexError("A ship already occupies that space. There is ship overlap")



ships = [
{
    "x": 2,
    "y": 1,
    "size": 4,
    "direction": "H",
    "name": "ship1"
},
{
    "x": 7,
    "y": 4,
    "size": 3,
    "direction": "V",
    "name": "ship2"
},
{
    "x": 3,
    "y": 5,
    "size": 2,
    "direction": "V",
    "name": "ship3"
},
{
    "x": 6,
    "y": 8,
    "size": 1,
    "direction": "H",
     "name": "ship4"
}
]
game_instance = BattleshipGameBoard()

for ship in ships:
       game_instance.add_ship(Ship(ship["x"],ship["y"],ship["direction"],ship["size"],ship["name"]))

game_instance.fillboard()

game_instance.print_board()

def get_col():
  while True:
    try:
      guess = int(input("Column Guess: "))
      if guess in range(1, 10 + 1):
        return guess
      else:
        print("\nOops, that's not even in the ocean.")
    except ValueError:
      print("\nPlease enter a number")

def get_row():
  while True:
    try:
      guess = int(input("Row Guess: "))
      if guess in range(1, 10 + 1):
        return guess
        print("\nOops, that's not even in the ocean.")
    except ValueError:
      print("\nPlease enter a number")


def Hit(x,y):
 for ship in game_instance.shipsonboard:
      if ship.contains(x,y):
        ship.coordinates[:] = [coord for coord in ship.coordinates if not (str(coord.get("row")) == str(x) and  str(coord.get("col")) == str(y))]


while(True):
    x = get_row()
    y = get_col()
    Hit(x,y)

    for ship in game_instance.shipsonboard:
        if ship.is_destroyed():
            print("destroyed {}".format(ship.ship_name))

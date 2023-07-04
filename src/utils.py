import numpy as np


class Boat:
    """
    Boat object
    """
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def get_length(self):
        """
        Get length of boat
        :return: int --> Length
        """
        return self.length

    def get_name(self):
        """
        Get name of boat
        :return: String --> name
        """
        return self.name

    def check_string(self):
        """
        Get first and last character of boat name
        :return: String --> First and last character
        """
        return self.name[0] + self.name[-1]


class PrincipalBoard:
    """
    Main board, with all boats
    """
    def __init__(self, dimensions, player):
        self.dimensions = dimensions
        self.player = player
        self.tablero = np.full(self.dimensions, '..')
        self.list_boats_coordinates = []
        self.list_boats_coordinates_copy = []

    def get_name(self):
        """
        Get player id
        :return: int --> Player id
        """
        return self.player

    def draw(self):
        """
        Draw the main board for each player
        :return: None
        """
        print("\t\t\t Mi Pantalla ------> JUGADOR {}".format(self.player))
        print("\t1\t 2\t  3\t   4\t5\t 6\t  7\t   8\t9\t10")
        print(self.tablero)

    def draw_boat(self, boat, coordinates, direction):
        """
        Draw the ship at a specific coordinate
        :param boat: Boat object
        :param coordinates: Tuple of coordinates
        :param direction: String --> horizontal or vertical
        :return:
        """
        x_point = coordinates[0]
        y_point = coordinates[1]
        boat_letter_name = boat.check_string()
        if direction == "h":
            if boat.get_length() + x_point > self.dimensions[0]:
                print("\tNo se puede colocar, excede los límites del tablero".upper())
                self.draw()
                return True
            elif not np.all(self.tablero[coordinates[1]:coordinates[1] + 1:1, coordinates[0]:coordinates[0] + boat.get_length():1] == '..'):
                print("\tNo se puede colocar, hay un barco en esa posición".upper())
                self.draw()
                return True
            else:
                self.tablero[coordinates[1]:coordinates[1] + 1:1, coordinates[0]:coordinates[0] + boat.get_length():1] = boat_letter_name
                y_coor = np.where(self.tablero == boat_letter_name)[0]
                x_coor = np.where(self.tablero == boat_letter_name)[1]
                x_y_coordinates = list(zip(x_coor, y_coor))
                self.list_boats_coordinates.append(x_y_coordinates)
                self.list_boats_coordinates_copy.append(x_y_coordinates.copy())
                self.draw()
                return False
        else:
            if boat.get_length() + y_point > self.dimensions[1]:
                print("\tNo se puede colocar, excede los límites del tablero".upper())
                self.draw()
                return True
            elif not np.all(self.tablero[coordinates[1]:coordinates[1] + boat.get_length():1, coordinates[0]:coordinates[0] + 1:1] == '..'):
                print("\tNo se puede colocar, hay un barco en esa posición".upper())
                self.draw()
                return True
            else:
                self.tablero[coordinates[1]:coordinates[1] + boat.get_length():1, coordinates[0]:coordinates[0] + 1:1] = boat_letter_name
                y_coor = np.where(self.tablero == boat_letter_name)[0]
                x_coor = np.where(self.tablero == boat_letter_name)[1]
                x_y_coordinates = list(zip(x_coor, y_coor))
                self.list_boats_coordinates.append(x_y_coordinates)
                self.list_boats_coordinates_copy.append(x_y_coordinates.copy())
                self.draw()
                return False

    def draw_shot(self, x, y, string):
        """
         Draw on the board the shot
        :param x: int --> 'X' Coordinate
        :param y: int --> 'Y' Coordinate
        :param string: String --> Character to draw
        :return: None
        """
        self.tablero[y][x] = string

    def check_win(self):
        """
        Check in each shot if all the ships are sunk
        :return: Boolean --> True, if there are no boats, False, if there are
        """
        if len(self.list_boats_coordinates) == 0:
            return True
        else:
            return False

    def check_shot(self, coordinates, shots_board):
        """
        Check what the shot has hit, and draw the corresponding characters on the board
        :param coordinates: Tuple --> Coordinates of shot
        :param shots_board: SecondaryBoard of player
        :return:
        """
        x_point = coordinates[0]
        y_point = coordinates[1]
        position = self.tablero[y_point][x_point]
        shots_position = shots_board.tablero[y_point][x_point]
        x_y_coordinates = (x_point, y_point)
        if position != ".." and position != "**" and position != "XX" and position != "HU":
            self.tablero[y_point][x_point] = "XX"
            shots_board.draw_shot(x_point, y_point, "XX")
            for coordinate_list in self.list_boats_coordinates:
                for coordinate in coordinate_list:
                    if coordinate == x_y_coordinates:
                        coordinate_list.remove(coordinate)
            print("\t\t\t ---------> TOCADO <---------")
            print("\t\t\t  --------> {} <-------".format((x_point + 1, y_point + 1)))
            index = 0
            copy_list = self.list_boats_coordinates.copy()
            while index < len(copy_list):
                if len(copy_list[index]) == 0:
                    print("\t\t\t ---------> HUNDIDO <---------")
                    for coordinate_tuple in self.list_boats_coordinates_copy[index]:
                        shots_board.draw_shot(coordinate_tuple[0], coordinate_tuple[1], "HU")
                        self.tablero[coordinate_tuple[1]][coordinate_tuple[0]] = "HU"
                    del self.list_boats_coordinates[index]
                    del self.list_boats_coordinates_copy[index]
                index += 1
                copy_list = self.list_boats_coordinates.copy()
            return True
        elif shots_position == "XX":
            print("\t\t\t----> BARCO YA TOCADO <----")
            print("\t\t\t --------> {} <--------".format((x_point + 1, y_point + 1)))
            return False
        elif shots_position == "OO":
            print("\t\t----> COORDENADA DE AGUA PREVIA <----")
            print("\t\t\t --------> {} <--------".format((x_point + 1, y_point + 1)))
            return False
        elif shots_position == "HU":
            print("\t\t----> COORDENADA DE BARCO HUNDIDO <----")
            print("\t\t\t --------> {} <--------".format((x_point + 1, y_point + 1)))
            return False
        else:
            print("\t\t\t ---------> AGUA <---------")
            print("\t\t\t  -------> {} <------- ".format((x_point + 1, y_point + 1)))
            shots_board.draw_shot(x_point, y_point, "**")
            return False


class SecondaryBoard(PrincipalBoard):
    """
    Secondary board, with shots made
    """
    def draw(self):
        """
        Draw the secondary(shots) board for each player
        :return: None
        """
        print("\t\t  Pantalla Disparos ------> JUGADOR {}".format(self.player))
        print("\t1\t 2\t  3\t   4\t5\t 6\t  7\t   8\t9\t10")
        print(self.tablero)

import numpy as np
import utils
from src.constants import DIMENSIONS, AIRCRAFTCARRIER, FRIGATE, CORBETA, HELANDION, INTRODUCTION, TITLE, MACHINE_VICTORY, PLAYER_VICTORY


def coordinates(dimensions):
    """
    Place the ships based on the entered coordinates
    :param dimensions: Dimensions of Board
    :return: Tuple --> Coordinate x and y, minus 1
    """
    coordinate_x = int(input("\tElige el punto en 'X' --> ".upper()))
    coordinate_y = int(input("\tElige el punto en 'Y' --> ").upper())
    if (coordinate_y > dimensions[1]) or (coordinate_x > dimensions[0]):
        print("COORDENADAS FUERA DEL LÍMITE DEL TABLERO, (1 - 10)")
        coordinates(DIMENSIONS)
    else:
        return coordinate_x - 1, coordinate_y - 1


def random_coordinates(dimensions):
    """
    Place ships based on randomly generated coordinates
    :param dimensions: Dimensions of Board
    :return: Tuple with coordinates x and y
    """
    coordinate_x = np.random.randint(0, dimensions[0])
    coordinate_y = np.random.randint(0, dimensions[1])
    coordinates_xy = (coordinate_x, coordinate_y)
    return coordinates_xy


def create_boards():
    """
    Create each board for each player
    :return: Tuple --> All boards for each player
    """
    p_board = utils.PrincipalBoard(DIMENSIONS, 1)
    p_s_board = utils.SecondaryBoard(DIMENSIONS, 1)
    m_board = utils.PrincipalBoard(DIMENSIONS, 2)
    m_s_board = utils.SecondaryBoard(DIMENSIONS, 2)

    return p_board, p_s_board, m_board, m_s_board


def create_boats():
    """
    Create all ships
    :return: List with all the boats
    """
    boats_list = []

    for x in range(AIRCRAFTCARRIER[1]):
        name = "Aircraft " + str(x + 1)
        boat = utils.Boat(AIRCRAFTCARRIER[0], name)
        boats_list.append(boat)

    for x in range(FRIGATE[1]):
        name = "Frigate " + str(x + 1)
        boat = utils.Boat(FRIGATE[0], name)
        boats_list.append(boat)

    for x in range(CORBETA[1]):
        name = "Corbeta " + str(x + 1)
        boat = utils.Boat(CORBETA[0], name)
        boats_list.append(boat)

    for x in range(HELANDION[1]):
        name = "Helandion " + str(x + 1)
        boat = utils.Boat(HELANDION[0], name)
        boats_list.append(boat)

    return boats_list


def draw_boats(boats_list, board, auto_or_not_choice):
    """
    Place the ships on the corresponding board
    :param boats_list: List of boats
    :param board: Player board
    :param auto_or_not_choice: If you want to automatically place the ships or not
    :return: None
    """
    if (board.get_name() == machine_board.get_name()) or (board.get_name() == player_board.get_name() and auto_or_not_choice == "si"):
        for boat in boats_list:
            boolean_check = True
            while boolean_check:
                coordinates_xy = random_coordinates(DIMENSIONS)
                number = np.random.randint(0, 2)
                if number == 0:
                    direction = "h"
                else:
                    direction = "v"
                boolean_check = board.draw_boat(boat, coordinates_xy, direction)
    else:
        for boat in boats_list:
            board.draw()
            print("\tColoca el {} --> Longitud {}".upper().format(boat.get_name(), boat.get_length()))
            if boat.get_length() == 1:
                direction = "v"
                boolean_check = True
                while boolean_check:
                    coordinates_x_y = coordinates(DIMENSIONS)
                    boolean_check = board.draw_boat(boat, coordinates_x_y, direction)
            else:
                boolean_check = True
                while boolean_check:
                    direction = input("\tVERTICAL (v) o HORIZONTAL (h) --> ")
                    coordinates_x_y = coordinates(DIMENSIONS)
                    boolean_check = board.draw_boat(boat, coordinates_x_y, direction)


def make_shot(player_turn, game_level):
    """
    Check what is in the coordinate, and based on this, mark if it is water, if it is a ship, if it is a previous coordinate...
    :param player_turn: Which player turn is, to shot
    :param game_level: Level chosen
    :return: Boolean that dictates if it shots again
    """
    if player_turn == player_board.get_name():
        coordinates_xy_shot = coordinates(DIMENSIONS)
        player_board.draw()
        success_bool = machine_board.check_shot(coordinates_xy_shot, player_shots_board)
        player_shots_board.draw()
        return success_bool
    elif player_turn == machine_board.get_name():
        boolean_set = set()
        if game_level == "f":
            shots = 1
        elif game_level == "m":
            shots = 2
        else:
            shots = 3
        for repetition in range(shots):
            coordinates_xy_shot = random_coordinates(DIMENSIONS)
            machine_board.draw()
            success_bool = player_board.check_shot(coordinates_xy_shot, machine_shots_board)
            machine_shots_board.draw()
            boolean_set.add(success_bool)
        if True in boolean_set:
            success_bool = True
            return success_bool
        else:
            success_bool = False
            return success_bool


def continue_playing(player_turn, success_condition):
    """
    Check if the game continues and who continues it
    :param player_turn: Which player turn is
    :param success_condition: Boolean that marks if the shot was successful, to continue shooting
    :return: Tuple --> Success Boolean (Check shot success), Flag Boolean (Checks if the game ended), Player Turn
    """
    if player_turn == player_board.get_name():
        if machine_board.check_win():
            print(PLAYER_VICTORY)
            success_condition = False
            flag_bool = False
            return success_condition, flag_bool, player_turn
    else:
        if player_board.check_win():
            print(MACHINE_VICTORY)
            success_condition = False
            flag_bool = False
            return success_condition, flag_bool, player_turn
    if not machine_board.check_win() and not player_board.check_win():
        choice = input("\t¿CONTINUAR JUGANDO? (si / no) -->")
        if choice == "si" and success_condition:
            print("\tDispara otra vez".upper())
            flag_bool = True
            if player_turn == player_board.get_name():
                player_turn = player_board.get_name()
                return success_condition, flag_bool, player_turn
            else:
                player_turn = machine_board.get_name()
                return success_condition, flag_bool, player_turn
        elif choice == "si" and not success_condition:
            flag_bool = True
            if player_turn == player_board.get_name():
                print("\tTurno del Jugador {}".upper().format(machine_board.get_name()))
                player_turn = machine_board.get_name()
                return success_condition, flag_bool, player_turn
            else:
                print("\tTurno del Jugador {}".upper().format(player_board.get_name()))
                player_turn = player_board.get_name()
                return success_condition, flag_bool, player_turn
        elif choice == "no":
            success_condition = False
            flag_bool = False
            player_turn = None
            return success_condition, flag_bool, player_turn


if __name__ == '__main__':
    print(TITLE)
    print(INTRODUCTION)
    player_board, player_shots_board, machine_board, machine_shots_board = create_boards()
    list_of_boats = create_boats()
    manual_or_auto = input("\t¿DESEAS COLOCAR LOS BARCOS AUTOMÁTICAMENTE? (si / no) --> ")
    draw_boats(list_of_boats, machine_board, manual_or_auto.lower())
    draw_boats(list_of_boats, player_board, manual_or_auto.lower())
    print("\tLos tableros están formados, empieza el juego, comienza el JUGADOR {}".upper().format(player_board.get_name()))
    level = input("\tESCOGE EL NIVEL DE DIFICULTAD: Fácil (f), Medio (m), Difícil (d) --> ")
    flag = True
    player = player_board.get_name()
    while flag:
        if player == player_board.get_name():
            success = True
            while success:
                player_board.draw()
                player_shots_board.draw()
                success = make_shot(player, None)
                success, flag, player = continue_playing(player, success)
        else:
            success = True
            while success:
                machine_board.draw()
                machine_shots_board.draw()
                success = make_shot(player, level)
                success, flag, player = continue_playing(player, success)

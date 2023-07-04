DIMENSIONS = (10, 10)
AIRCRAFTCARRIER = (4, 1)
FRIGATE = (3, 2)
CORBETA = (2, 3)
HELANDION = (1, 4)
TITLE = """
██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ██╗██████╗     ██╗      █████╗     ███████╗██╗      ██████╗ ████████╗ █████╗ 
██║  ██║██║   ██║████╗  ██║██╔══██╗██║██╔══██╗    ██║     ██╔══██╗    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔══██╗
███████║██║   ██║██╔██╗ ██║██║  ██║██║██████╔╝    ██║     ███████║    █████╗  ██║     ██║   ██║   ██║   ███████║
██╔══██║██║   ██║██║╚██╗██║██║  ██║██║██╔══██╗    ██║     ██╔══██║    ██╔══╝  ██║     ██║   ██║   ██║   ██╔══██║
██║  ██║╚██████╔╝██║ ╚████║██████╔╝██║██║  ██║    ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║   ██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                                                                                                
"""
INTRODUCTION = """
Bienvenido a Hundir La Flota!, las instrucciones de este juego son muy sencillas:
- Un tablero de 10 x 10, las coordenadas se encuentras entre 1 y 10 --> (1, 5), (10, 6), (4, 8) ...
- Existen 3 niveles de dificultad para la máquina: FÁCIL (1 Disparo), MEDIO (2 Disparos), DIFÍCIL (3 Disparos)
- Si se acierta un disparo, se vuelve a disparar
- La máquina es el Jugador 2, y tu serás el Jugador 1
- El juego termina, cuando uno de los dos hunda todos los barcos del contrario, o si deseas terminar antes, podrás hacerlo después de cada disparo
- Si eliges colocar los barcos manualmente, por defecto la orientación HORIZONTAL pondrá el barco hacia la DERECHA, si es VERTICAL, se pondrá hacia ABAJO

COMIENZA EL JUEGO!
"""
MACHINE_VICTORY = """
                                                                                           
                            __                   _              ___                        
                         __|  | _ _  ___  ___  _| | ___  ___   |_  |                       
                        |  |  || | || . || .'|| . || . ||  _|  |  _|   _                   
                        |_____||___||_  ||__,||___||___||_|    |___|  | |                  
                                    |___|                             |_|                  
                                                                                        __ 
 _____         _____                   _         _____  _       __                     |  |
|  |  | ___   |   __| ___  ___  ___  _| | ___   |   __|| |   __|  | _ _  ___  ___  ___ |  |
|     || .'|  |  |  || .'||   || .'|| . || . |  |   __|| |  |  |  || | || -_|| . || . ||__|
|__|__||__,|  |_____||__,||_|_||__,||___||___|  |_____||_|  |_____||___||___||_  ||___||__|
                                                                             |___|         
"""
PLAYER_VICTORY = """
                                                                                           
                            __                   _              ___                        
                         __|  | _ _  ___  ___  _| | ___  ___   |_  |                       
                        |  |  || | || . || .'|| . || . ||  _|   _| |_    _                 
                        |_____||___||_  ||__,||___||___||_|    |_____|  | |                
                                    |___|                               |_|                
                                                                                        __ 
 _____         _____                   _         _____  _       __                     |  |
|  |  | ___   |   __| ___  ___  ___  _| | ___   |   __|| |   __|  | _ _  ___  ___  ___ |  |
|     || .'|  |  |  || .'||   || .'|| . || . |  |   __|| |  |  |  || | || -_|| . || . ||__|
|__|__||__,|  |_____||__,||_|_||__,||___||___|  |_____||_|  |_____||___||___||_  ||___||__|
                                                                             |___|         
"""
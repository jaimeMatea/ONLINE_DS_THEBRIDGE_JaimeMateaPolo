import numpy as np
import random
import time
from utils import crea_barco_aleatorio
from utils import recibir_disparo

def iniciar():

    tablero1=np.full((10,10), ' ') #tablero de los barcos del jugador 2
    tablero2=np.full((10,10), ' ') #tablero de los barcos del jugador 1
    tablero1_marcar=np.full((10,10), ' ') #tablero de las posiciones que ha marcado el jugador 1
    tablero2_marcar=np.full((10,10), ' ') #tablero de las posiciones que ha marcado el jugador 2

    #Creación tablero inicial j1
    tablero1 = crea_barco_aleatorio(tablero1,2)
    tablero1 = crea_barco_aleatorio(tablero1,2)
    tablero1 = crea_barco_aleatorio(tablero1,2)
    tablero1 = crea_barco_aleatorio(tablero1,3)
    tablero1 = crea_barco_aleatorio(tablero1,3)
    tablero1 = crea_barco_aleatorio(tablero1,4)

    #Creación tablero inicial j2
    tablero2 = crea_barco_aleatorio(tablero2,2)
    tablero2 = crea_barco_aleatorio(tablero2,2)
    tablero2 = crea_barco_aleatorio(tablero2,2)
    tablero2 = crea_barco_aleatorio(tablero2,3)
    tablero2 = crea_barco_aleatorio(tablero2,3)
    tablero2 = crea_barco_aleatorio(tablero2,4)

    jugador1=input("Introduce tu nombre, jugador 1:")

    num_x_1=0
    num_x_2=0

    while num_x_1<16 and num_x_2<16:

        # Ronda
        print(f"""TURNO DEL {jugador1}\n****************""")
        x1=int(input(f"{jugador1}: Introduce la coordenada x del barco que quieres derribar:"))
        y1=int(input(f"{jugador1}: Introduce la coordenada y del barco que quieres derribar:"))
        print(recibir_disparo(tablero1,(x1,y1)))
        recibir_disparo(tablero1_marcar,(x1,y1))
        if recibir_disparo(tablero1,(x1,y1))==True:
            
            num_x_1+=1            
        print(num_x_1)
        print(tablero1)
        #print(tablero1_marcar)
        time.sleep(2)

        print(f"""\nTURNO DEL JUGADOR 2\n*******************""")
        x2=np.random.randint(0,9)
        y2=np.random.randint(0,9)
        print(recibir_disparo(tablero2,(x2,y2)))
        recibir_disparo(tablero2_marcar,(x2,y2))
        if recibir_disparo(tablero2,(x1,y1))==True:
            num_x_2+=1
        print(num_x_2)
        print(tablero2)
        #print(tablero2_marcar)
        break

    if num_x_1==16:
        print(f"{jugador1} ha ganado")
    if num_x_2==16:
        print("Jugador 2 ha ganado")

    #print(tablero1)
    #print(tablero2)
    #print(tablero1_marcar)


if __name__ == "__main__":
    iniciar()
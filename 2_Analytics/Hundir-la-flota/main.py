import numpy as np
import time
from utils import crea_barco_aleatorio,recibir_disparo

def iniciar():

    tablero1=np.full((10,10),'~') #tablero de los barcos del jugador 1
    tablero2=np.full((10,10),'~') #tablero de los barcos del jugador 2
    tablero1_marcar=np.full((10,10),'~') #tablero del radar del tablero del jugador 2
    tablero2_marcar=np.full((10,10),'~') #tablero del radar del tablero del jugador 1

    dict_barcos_j1={"Destructor (size 2)":0, "Acorazado (size 3)":0, "Portaaviones (size 4)":0}
    dict_barcos_j2={"Destructor (size 2)":0, "Acorazado (size 3)":0, "Portaaviones (size 4)":0}

    # #Creación tablero inicial j1
    # tablero1 = crea_barco_aleatorio(tablero1,2,dict_barcos_j1)
    # tablero1 = crea_barco_aleatorio(tablero1,2,dict_barcos_j1)
    # tablero1 = crea_barco_aleatorio(tablero1,2,dict_barcos_j1)
    # tablero1 = crea_barco_aleatorio(tablero1,3,dict_barcos_j1)
    # tablero1 = crea_barco_aleatorio(tablero1,3,dict_barcos_j1)
    # tablero1 = crea_barco_aleatorio(tablero1,4,dict_barcos_j1)

    # #Creación tablero inicial j2
    # tablero2 = crea_barco_aleatorio(tablero2,2,dict_barcos_j2)
    # tablero2 = crea_barco_aleatorio(tablero2,2,dict_barcos_j2)
    # tablero2 = crea_barco_aleatorio(tablero2,2,dict_barcos_j2)
    # tablero2 = crea_barco_aleatorio(tablero2,3,dict_barcos_j2)
    # tablero2 = crea_barco_aleatorio(tablero2,3,dict_barcos_j2)
    # tablero2 = crea_barco_aleatorio(tablero2,4,dict_barcos_j2)


    barcos_j1=[]
    barcos_j2=[]
    esloras=[2,2,2,3,3,4]

    # Creación barcos iniciales j1
    for i in esloras:
        tablero1,barco1=crea_barco_aleatorio(tablero1,i,dict_barcos_j1)
        barco_eslora=[i,barco1]
        barcos_j1.append(barco_eslora)
        print(barco_eslora)

    # Creación barcos iniciales j2
    for i in esloras:
        tablero2,barco2=crea_barco_aleatorio(tablero2,i,dict_barcos_j2)
        barco_eslora=[i,barco2]
        barcos_j2.append(barco_eslora)



    jugador1=input("Introduce tu nombre, jugador 1: ")

    num_x_1=0
    num_x_2=0

    while num_x_1<16 and num_x_2<16:

        # Ronda
        print(f"""TURNO DE {jugador1}\n****************""")
        x1=int(input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar: "))
        y1=int(input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar: "))

        disparo_j1 = recibir_disparo(tablero2,(x1,y1),dict_barcos_j2,barcos_j2)
        if disparo_j1:
            num_x_1+=1
            tablero1_marcar[(x1,y1)]="X"
        else:
            if tablero2[(x1,y1)]=="-":
                tablero1_marcar[(x1,y1)]="-"
                
        print(f"Puntos de {jugador1}: {num_x_1}")
        print("Radar del jugador 2:")
        print(tablero1_marcar)

        time.sleep(2)




    
        print(f"""\nTURNO DEL JUGADOR 2\n*******************""")
        x2=np.random.randint(0,9)
        y2=np.random.randint(0,9)

        disparo_j2 = recibir_disparo(tablero1,(x2,y2),dict_barcos_j1,barcos_j1)
        if disparo_j2:
            num_x_2+=1
            tablero2_marcar[(x2,y2)]="X"
        else:
            if tablero1[(x2,y2)]=="-":
                tablero2_marcar[(x2,y2)]="-"
                
        print(f"Puntos del jugador 2: {num_x_2}\n\n")


    if num_x_1==16:
        print(f"{jugador1} ha ganado")
    if num_x_2==16:
        print("Jugador 2 ha ganado")







if __name__ == "__main__":
    iniciar()
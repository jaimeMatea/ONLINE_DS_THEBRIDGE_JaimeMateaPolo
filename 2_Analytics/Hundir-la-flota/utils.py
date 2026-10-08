import numpy as np
import random

#???????????????
def crea_tablero(lado):
    tablero = np.full((lado,lado)," ")
    return tablero


def comprueba_coordenada_x(x1,jugador1):
    while x1>10 or x1<1:
        if x1>10:
            print("Demasiado alto, introduce un número en la coordenada x entre 1 y 10, prueba otra vez")
            x1=int(input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): "))
        elif x1<1:
            print("Demasiado bajo, introduce un número en la coordenada x entre 1 y 10, prueba otra vez")
            x1=int(input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): "))
        # elif str(x1)=="":
        #     print("Ningun valor introducido, introduce un número en la coordenada x entre 1 y 10, prueba otra vez")
        #     x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
        # elif x1.isalpha:
        #     print("El caracter no se admite, prueba otra vez")
        #     x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
    return x1


def comprueba_coordenada_y(y1,jugador1):
    while y1>10 or y1<1:
        if y1>10:
            print("Demasiado alto, introduce un número en la coordenada y entre 1 y 10, prueba otra vez")
            y1=int(input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al 10): "))
        elif y1<1:
            print("Demasiado bajo, introduce un número en la coordenada y entre 1 y 10, prueba otra vez")
            y1=int(input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al 10): "))
        # elif str(y1)=="":
        #     print("Ningun valor introducido, introduce un número en la coordenada y entre 1 y 10, prueba otra vez")
        #     y1=input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al 10): ")
        # elif y1.isalpha:
        #     print("El caracter no se admite, prueba otra vez")
        #     y1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
    return y1


def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            return False
        if columna <0 or columna>= num_max_columnas:
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp


def dic_barcos(dict_barcos,barco):
    if len(barco)==2:
        dict_barcos["Destructor (size 2)"]+=1
    elif len(barco)==3:
        dict_barcos["Acorazado (size 3)"]+=1
    elif len(barco)==4:
        dict_barcos["Portaaviones (size 4)"]+=1
    return dict_barcos


def crea_barco_aleatorio(tablero,eslora,dict_barcos):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        posicion_inicial = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(posicion_inicial)
        orientacion = random.choice(["N","S","O","E"])
        fila = posicion_inicial[0]
        columna = posicion_inicial[1]
        for i in range(eslora-1):
            if orientacion=="N":
                fila-=1
            elif orientacion=="S":
                fila+=1
            elif orientacion=="E":
                columna+=1
            else:
                columna-=1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            #print(dic_barcos(dict_barcos,barco))
            dic_barcos(dict_barcos,barco)
            return tablero_temp,barco


def recibir_disparo(tablero,coordenada,dict_barcos,barcos,jugador):
    if tablero[coordenada]=="O":
        tablero[coordenada]="X"
        print(f"Tocado, en la coordenada {coordenada}")
        for i in barcos:
            eslora_antigua=i[0]
            coordenadas_antiguas=i[1]
            if coordenada in coordenadas_antiguas:
                coordenadas_antiguas.remove(coordenada)
                if len(coordenadas_antiguas)==0:
                    if eslora_antigua==2:
                        dict_barcos["Destructor (size 2)"]-=1
                        print("Destructor hundido\n")
                        print(f"Barcos restantes del rival: {dict_barcos}\n")
                    elif eslora_antigua==3:
                        dict_barcos["Acorazado (size 3)"]-=1
                        print("Acorazado hundido\n")
                        print(f"Barcos restantes del rival: {dict_barcos}\n")
                    elif eslora_antigua==4:
                        dict_barcos["Portaaviones (size 4)"]-=1
                        print("Portaaviones hundido\n")
                        print(f"Barcos restantes del rival: {dict_barcos}\n")
                break
        return True
    elif tablero[coordenada]=="X":
        if jugador!="Jugador 2":
            print("Ese barco ya ha sido golpeado en ese sitio, prueba otra vez")
            return False
    elif tablero[coordenada]=="-":
        if jugador!="Jugador 2":
            print("Esa casilla de mar ya ha sido golpeada en ese sitio. prueba otra vez")
            return False
    else:
        tablero[coordenada]="-"
        print("Agua")
        return True
import numpy as np
import random

def imprimir_tablero_color(tablero):
    for i in tablero:
        fila_coloreada = []
        for j in i:
            if j=="X":
                #fila_coloreada.append("\033[31mX\033[0m") # Rojo
                fila_coloreada.append("🔥")
            elif j=="-":
                #fila_coloreada.append("\033[33m-\033[33m") # Amarillo
                fila_coloreada.append("💦")
            elif j=="~":
                #fila_coloreada.append("\033[34m~\033[0m") # Azul
                fila_coloreada.append("🌊")
            elif j=="O":
                fila_coloreada.append("🚢")
        print(" ".join(fila_coloreada))
    print()


def menu():
    print("""
    ╔════════════════════════════╗
    ║     JUEGO DEL AHORCADO     ║
    ╚════════════════════════════╝

    [1] 🎮 COMENZAR BATALLA
        
    [2] ❌ SALIR DEL JUEGO

    \x1B[3m-Escribe la palabrea 'salir' en cualquier momento para cancelar la partida y volver al menú-\x1B[0m
    """)
    entrada=int(input(""))
    print("\n")
    return entrada


def comprueba_coordenada_x(x1,jugador1,tablero1):
    if x1=="salir":
        return x1
    x1=int(x1)
    while x1>tablero1.shape[0] or x1<1:
        if x1>tablero1.shape[0]:
            print(f"Demasiado alto, introduce un número en la coordenada x entre 1 y {tablero1.shape[0]}, prueba otra vez")
            x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al {tablero1.shape[0]}): ")
        elif x1<1:
            print(f"Demasiado bajo, introduce un número en la coordenada x entre 1 y {tablero1.shape[0]}, prueba otra vez")
            x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al {tablero1.shape[0]}): ")
        # elif str(x1)=="":
        #     print("Ningun valor introducido, introduce un número en la coordenada x entre 1 y 10, prueba otra vez")
        #     x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
        # elif x1.isalpha:
        #     print("El caracter no se admite, prueba otra vez")
        #     x1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
    return x1


def comprueba_coordenada_y(y1,jugador1,tablero1):
    if y1=="salir":
            return y1
    y1=int(y1)
    while y1>tablero1.shape[1] or y1<1:
        if y1>tablero1.shape[1]:
            print(f"Demasiado alto, introduce un número en la coordenada y entre 1 y {tablero1.shape[1]}, prueba otra vez")
            y1=input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al {tablero1.shape[1]}): ")
        elif y1<1:
            print(f"Demasiado bajo, introduce un número en la coordenada y entre 1 y {tablero1.shape[1]}, prueba otra vez")
            y1=input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al {tablero1.shape[1]}): ")
        # elif str(y1)=="":
        #     print("Ningun valor introducido, introduce un número en la coordenada y entre 1 y 10, prueba otra vez")
        #     y1=input(f"{jugador1}, introduce la coordenada y del barco que quieres derribar (numero del 1 al 10): ")
        # elif y1.isalpha:
        #     print("El caracter no se admite, prueba otra vez")
        #     y1=input(f"{jugador1}, introduce la coordenada x del barco que quieres derribar (numero del 1 al 10): ")
    return y1


def dic_barcos(dict_barcos,barco):
    if len(barco)==2:
        dict_barcos["Destructor (size 2)"]+=1
    elif len(barco)==3:
        dict_barcos["Acorazado (size 3)"]+=1
    elif len(barco)==4:
        dict_barcos["Portaaviones (size 4)"]+=1
    return dict_barcos


def coloca_barco_plus(tablero, barco):
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


def crea_barco_aleatorio(tablero,eslora,dict_barcos):
    while True:
        barco=[]
        posicion_inicial = (random.randint(0,tablero.shape[0]-1),random.randint(0,tablero.shape[1]-1))
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
            pieza=(fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            dic_barcos(dict_barcos,barco)
            return tablero_temp,barco


def crea_barco_aleatorio_j1(tablero,eslora,dict_barcos,jugador):    
    dict_nombres = {2: "Destructor (size 2)", 3: "Acorazado (size 3)", 4: "Portaaviones (size 4)"}
    nombre_barco = dict_nombres[eslora]

    while True:
        print(f"Coloca el barco --> {nombre_barco}")
        try:
            fila=int(input(f"{jugador}, introduce la fila inicial (1 al {tablero.shape[0]}): "))-1
            # if fila=="salir":
            #     return "salir"
            columna=int(input(f"{jugador}, introduce la columna inicial (1 al {tablero.shape[1]}): "))-1
        except ValueError:
            print("El numero es incorrecto, introduce uno válido")
            continue

        orientacion=input("Introduce la orientación (N / S / E / O): ").strip().upper()
        if orientacion not in ["N","S","E","O"]:
            print("La orientación no es correcta. Debe ser N, S, E u O")
            continue

        barco=[]
        posicion_inicial = (fila,columna)
        barco.append(posicion_inicial)
        
        for i in range(eslora-1):
            if orientacion=="N":
                fila-=1
            elif orientacion=="S":
                fila+=1
            elif orientacion=="E":
                columna+=1
            else:
                columna-=1
            pieza=(fila,columna)
            barco.append(pieza)
        tablero_temp=coloca_barco_plus(tablero,barco)
        if type(tablero_temp)==np.ndarray:
            dic_barcos(dict_barcos,barco)
            print("Barco colocado correctamente\n")
            print(tablero_temp)
            return tablero_temp,barco
        else:
            print("El barco se sale del mapa o choca con otro barco, prueba otra vez")


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
                        print("Destructor hundido 🔥☠️\n")
                        print(f"Barcos restantes del rival: {dict_barcos}\n")
                    elif eslora_antigua==3:
                        dict_barcos["Acorazado (size 3)"]-=1
                        print("Acorazado hundido 🔥☠️\n")
                        print(f"Barcos restantes del rival: {dict_barcos}\n")
                    elif eslora_antigua==4:
                        dict_barcos["Portaaviones (size 4)"]-=1
                        print("Portaaviones hundido 🔥☠️\n")
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
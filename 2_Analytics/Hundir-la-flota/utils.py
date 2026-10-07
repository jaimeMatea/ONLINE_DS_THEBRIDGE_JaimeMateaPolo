import numpy as np
import random
import time

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

def crea_barco_aleatorio(tablero,eslora, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        #ELEGIR EL JUGADOR 1 LA POSICION?????
        posicion_inicial = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(posicion_inicial)
        orientacion = random.choice(["N","S","O","E"])
        fila = posicion_inicial[0]
        columna = posicion_inicial[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada]=="O":
        tablero[coordenada]="X"
        #return f"Tocado, en la coordenada {coordenada}",True
        print(f"Tocado, en la coordenada {coordenada}")
        return True
    elif tablero[coordenada]=="X":
        return "Ese barco ya ha sido golpeado en ese sitio"
    else:
        tablero[coordenada]="-"
        return "Agua"
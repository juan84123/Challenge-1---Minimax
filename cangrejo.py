#Crea una funcion crear_tablero, creando la matriz con un bucle for anidado.
#Ubica en el tablero G para gato y R para raton.
#crea otra funcion imprimir_tablero usando un .join.
#Imprime el tablero.

tamano_x = 5
tamano_y = 5
tablero = []

def crear_tablero():
    tablero = []
    aux = "."
    for fila in range(tamano_x):
        fila = []
        for columna in range(tamano_y):
            fila.append(aux)
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    for i in range(tamano_x):
        fila = " ".join(tablero[i])
        print(fila)
    
tablero = crear_tablero()

tablero[0][1] = "R" 
tablero[1][0] = "G"

imprimir_tablero(tablero)


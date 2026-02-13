import random

tamano_x = 5            #Tamano i de la matriz
tamano_y = 5            #Tamano j de la matriz
tablero = []            #Tablero de juego

def crear_tablero():
    for fila in range(tamano_x):
       fila = [] # Se crea una lista (fila) vacia
       for columna in range(tamano_y):  
           fila.append(".") # Se meten los 0 en la fila 1 por 1
       tablero.append(fila) # Se agrega la fila a la matriz

def imprimir_tablero():
    for i in tablero:
        for j in i:
            print(" ",j,end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
        print(" ")

def colocar_personaje(personaje):
    while True: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero[i][j] == ".":
            tablero[i][j] = personaje
            return i,j   #retorna lo las posiciones

def fun_de_mov_human(eleccion_jugador):
    mov = input(f"Donde desdea mover:\n"
        "   w     \n"
        "a     d  \n"
        "   s     \n"
        "Elección: ")
    return mov

def movimineto_valido(mov, elecc):
    if elecc == 1:
        i = pos_gato[0]
        j = pos_gato[1]
    else:
        i = pos_raton[0]
        j = pos_raton[1]

    #poner un if, si es gato mira solo 4 opciones de movimiento, si es raton mira 8
    #se puede mejorar el codigo return (x - 1) >= 0 sin usar else
    if mov == "w":
        return (i - 1) >= 0 #pos[0]-1 >= 0, se toma este valor para corroborar que no desborde por arriba
    elif mov == "s":
        return (i + 1) < tamano_x #pos[0] + 1 <= tamano_x, para que no desborde por abajo
    elif mov == "d":
        return (j + 1) < tamano_y #pos[1]+1 <= tamano_y, para que no desborde por la derecha
    elif mov == "a":
        return (j - 1) >= 0 #pos[1]-1 <= 0, para que no desborde por la izquierda
    else:
        return False      

def mover_ficha(mov, elecc_humano):
    if elecc_humano == 1: #para saber si modificar gato o raton
        i = pos_gato[0]
        j = pos_gato[1]
    else:
        i = pos_raton[0]
        j = pos_raton[1]

    tablero[i][j] = 0 #para el lugar donde esta ahora se borre
 #poner un if, si es gato mira solo 4 opciones de movimiento, si es raton mira 8

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1

    tablero[i][j] = elecc_humano #Hace el cambio en el tablero

    if elecc_humano == 1: # guarda la nueva posicion de la ficha juagada
        pos_gato[0] = i
        pos_gato[1] = j
    else:
        pos_raton[0] = i
        pos_raton[1] = j

crear_tablero()
print("Juego del Gato y Raton")
imprimir_tablero()
pos_gato = list(colocar_personaje("G"))
pos_raton = list(colocar_personaje("R"))

eleccion_jugador = input("Desea ser:\ng : Gato \nr : Raton\nElección: ")

turno_actual = eleccion_jugador

while True:
    imprimir_tablero()
    if turno_actual == eleccion_jugador:
        mov = fun_de_mov_human(eleccion_jugador)
        if movimineto_valido(mov, eleccion_jugador):
            mover_ficha(mov, eleccion_jugador)
        else:
            print("Ese movimiento no es valido")

        pass
    else:

        pass
    pass
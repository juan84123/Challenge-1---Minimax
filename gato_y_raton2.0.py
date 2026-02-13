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
            print(" ", j, end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
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

def movimineto_valido(mov, pos):
    i = pos[0]
    j = pos[1]

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

def mover_ficha(mov, ficha, pos):
    i = pos[0]
    j = pos[1]

    tablero[i][j] = "." #para el lugar donde esta ahora se borre

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1

    tablero[i][j] = ficha #Hace el cambio en el tablero

    return i,j 

def corroborar_fin(cant_turno, pos_1,  pos_2):
    if  cant_turno == 0:
        print("El RATON se escapo")
        return True
    elif pos_1 == pos_2:
        tablero[pos_1[0]][pos_1[1]] = "G"
        print("El GATO comio al raton")        
        return True
    else:
        return False

def cambiar_turno(turno_actual):
    if turno_actual == "G":
        turno_actual = "R"
    else:
        turno_actual = "G"
    return turno_actual

crear_tablero()
cant_turno = 50
print("Juego del Gato y Raton")
imprimir_tablero()
pos_gato = list(colocar_personaje("G"))
pos_raton = list(colocar_personaje("R"))
ficha_jugador = input("Desea ser:\ng : Gato \nr : Raton\nElección: ")

if ficha_jugador == "G":
    pos_jugador = pos_gato
    pos_ai = pos_raton
else:
    pos_jugador = pos_raton
    pos_ai = pos_gato

turno_actual = ficha_jugador

while True:
    imprimir_tablero()
    if turno_actual == ficha_jugador:         
        mov = fun_de_mov_human(ficha_jugador)
        if movimineto_valido(mov, pos_jugador):
            pos_jugador = list(mover_ficha(mov, ficha_jugador, pos_jugador))
            cant_turno -= 1
            turno_actual = cambiar_turno(turno_actual)
            print(turno_actual)
        else:
            print("Ese movimiento no es valido")
    else:
        print("Turno de la IA")

        turno_actual = cambiar_turno(turno_actual)
    
    if corroborar_fin(cant_turno, pos_jugador, pos_ai):
        break
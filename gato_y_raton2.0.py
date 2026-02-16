import random

tamano_x = 5            #Tamano i de la matriz
tamano_y = 5            #Tamano j de la matriz
cant_turno = 50
#tablero = []            #Tablero de juego

def crear_tablero():
    tablero = []
    for fila in range(tamano_x):
       fila = [] # Se crea una lista (fila) vacia
       for columna in range(tamano_y):  
           fila.append(".") # Se meten los 0 en la fila 1 por 1
       tablero.append(fila) # Se agrega la fila a la matriz
    return tablero

def imprimir_tablero(tablero_de_juego):
    for i in tablero_de_juego:
        for j in i:
            print(" ", j, end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
        print(" ")

def colocar_personaje(personaje, tablero_de_juego):
    while True: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero_de_juego[i][j] == ".":
            tablero_de_juego[i][j] = personaje
            return i,j   #retorna lo las posiciones

def fun_de_mov_human(mov):
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

def mover_ficha(mov, ficha, pos,tablero_de_juego):
    i = pos[0]
    j = pos[1]

    tablero_de_juego[i][j] = "." #para el lugar donde esta ahora se borre

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1

    tablero_de_juego[i][j] = ficha #Hace el cambio en el tablero

    return i,j 

def corroborar_fin(cant_turno, pos_1,  pos_2, tablero_de_juego):
    if  cant_turno == 0:
        print("El RATON se escapo")
        return True
    elif pos_1 == pos_2:
        tablero_de_juego[pos_1[0]][pos_1[1]] = "G"
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

#faltan ajustar los parametros
def dit_manhatan(pos_gato,pos_raton):

    dist_manh = abs(pos_gato[0]-pos_raton[0]) + abs(pos_gato[1]-pos_raton[1])
    return dist_manh

tablero_de_juego = crear_tablero()
print("Juego del Gato y Raton")
pos_gato = list(colocar_personaje("G",tablero_de_juego))
pos_raton = list(colocar_personaje("R",tablero_de_juego))
imprimir_tablero(tablero_de_juego)

#Guarda la ficha y la hace que sea mayuscula
ficha_jugador = input("Desea ser:\nG : Gato \nR : Raton\nElección: ").upper()

turno_actual = ficha_jugador

while True:
    imprimir_tablero(tablero_de_juego)
    if turno_actual == "G":
        print("Truno del Gato")
    else:
        print("Turno del Raton")
    if turno_actual == ficha_jugador:         
        mov = fun_de_mov_human(ficha_jugador)
        if ficha_jugador == "G":
            if movimineto_valido(mov, pos_gato):
                pos_gato = list(mover_ficha(mov, "G", pos_gato,tablero_de_juego))
                cant_turno -= 1
                turno_actual = cambiar_turno(turno_actual)
                print(turno_actual)
            else:
                print("Ese movimiento no es valido")
        else: 
            if movimineto_valido(mov, pos_raton):
                pos_raton = list(mover_ficha(mov, "R", pos_raton,tablero_de_juego))
                cant_turno -= 1
                turno_actual = cambiar_turno(turno_actual)
                print(turno_actual)
            else:
                print("Ese movimiento no es valido")

    else:
        print("Turno de la IA")

        turno_actual = cambiar_turno(turno_actual)
    
    if corroborar_fin(cant_turno, pos_gato, pos_raton,tablero_de_juego):
        imprimir_tablero(tablero_de_juego)
        break
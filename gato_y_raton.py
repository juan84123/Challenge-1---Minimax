import random
tamano_x = 5    #tamano i de la matriz
tamano_y = 3    #tamano j de la matriz
cant_turno = 5   #Para finalizar el juego
tablero = []     #tablero de juego
tablero_estetico = []
pos_gato = []    #posicion del gato
pos_raton = []   #posicion del raton
turno_actual = 0

#funcion que crea el tablero y lo llena de 0
def crear_tablero():
    for fila in range(tamano_x):
       fila = [] # Se crea una lista (fila) vacia
       for columna in range(tamano_y):  
           fila.append(0) # Se meten los 0 en la fila 1 por 1
       tablero.append(fila) # Se agrega la fila a la matriz

#funcion para imprimir el tablero, mas adelante, ver de imprimir con letras, o si es conveniente usar nomas letra
def imprimir_tablero():
    for i in tablero:
        for j in i:
            print(" ",j,end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
        print(" ")

#Esta funcion vaservir a modo que se vea estetico el juego el otro es solo para logica
def imprimir_tablero_estetico():
    for i in tablero:
        for j in i:
            if j == 0: print(" "," \u00B7 ",end="")
            elif j == 1: print(" ","🐱",end="") #al poner los emojis la matriz cambia, y ya no es estetica
            else: print(" ","🐭",end="")
        print(" ")
            #if fila == 0: print(".")
   
#Posibles problemas, si el random hace que esten my cerca, o si dan el mismo numero
def colocar_personaje(personaje):
    i = random.randint(0, tamano_x - 1) #genera un valor random para el eje x
    j = random.randint(0, tamano_y - 1) #genera un valor random para el eje y
    while tablero[i][j] != personaje: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero[i][j] == 0:
            tablero[i][j] = personaje
    return i,j   #retorna lo las posiciones

#Se encarga de imprimir a donde desea mover el humano, y llamar a las funciones que corroboran el movimiento y que hace el movimiento
def fun_de_mov_human(elecc_humano):
    mov = input(f"donde desdea mover? \nw - Arriba \ns - Abajo  \nd - Derecha \na - Izquierda\n")
    if movimineto_valido(mov, elecc_humano): # movimiento valido que sea true or false
        mover_ficha(mov, elecc_humano)
        return True
    else:
        print("Ese movimiento no es valido")
        return False

#Cambia el turno
def cambiar_turno():
    global turno_actual
    if turno_actual == 1:
        turno_actual = 2
    else:
        turno_actual = 1

#Corroborar si se puede mover a donde se quiere, da true o false, si el movimiento se puede o no hacer
def movimineto_valido(mov, elecc_humano):
    if elecc_humano == 1:
        x = pos_gato[0]
        y = pos_gato[1]
    else:
        x = pos_raton[0]
        y = pos_raton[1]

    print(x,y)

    if mov == "w":
        if (x-1) >= 0: #pos[0]-1 >= 0, se toma este valor para corroborar que no desborde por arriba
            return True
        else:
            return False
    elif mov == "s":
        if (x + 1) < tamano_x: #pos[0] + 1 <= tamano_x, para que no desborde por abajo
            return True
        else:
            return False
    elif mov == "d":
        if (y+1) < tamano_y: #pos[1]+1 <= tamano_y, para que no desborde por la derecha
            return True
        else:
            return False
    elif mov == "a":
        if (y-1) >= 0: #pos[1]-1 <= 0, para que no desborde por la izquierda
            return True
        else:
            return False

#Funcion funciona mal, no se cambia la pocion del gato ni el raton que es global
def mover_ficha(mov, elecc_humano):
    if elecc_humano == 1: #para saber si modificar gato o raton
        i = pos_gato[0]
        j = pos_gato[1]
    else:
        i = pos_raton[0]
        j = pos_raton[1]

    tablero[i][j] = 0 #para el lugar donde esta ahora se borre

    if mov == "w": #Mueve las piezas, arriba
        i = i - 1
    elif mov == "s": #Mueve las piezas, abajo
        i = i + 1
    elif mov == "d": #Mueve las piezas, derecha
        j = j + 1
    elif mov == "a": #Mueve las piezas, izquierda
        j = j - 1
   
    tablero[i][j] = elecc_humano #Hace el cambio en el tablero

    if elecc_humano == 1: # guarda la nueva posicion de la ficha juagada
        pos_gato[0] = i
        pos_gato[1] = j
    else:
        pos_raton[0] = i
        pos_raton[1] = j

#Corrobora el fin de juego, lo que falta es que cant_turnos disminuya, cada jugada
def corroborar_fin():
    if  cant_turno == 0:
        print("El RATON se escapo")
        return True
    elif pos_gato == pos_raton:
        #tablero[pos_gato[0]][pos_gato[0]] = "G"
        print("El GATO comio al raton")        
        return True
    else:
        return False

print("Juego del gato y raton")
crear_tablero()
pos_gato = list(colocar_personaje(1)) #se usa list para que el valor que retorna sea una lista y no tupla
pos_raton = list(colocar_personaje(2))
#hacer una funcion o en la misma de colocar personaje, que se encargue de que si estan muy cerca separe los personajes
print(pos_gato,pos_raton)
#imprimir_tablero()
imprimir_tablero_estetico()
elecc_humano = int(input("Desea ser:\n1 : Gato \n2 : Raton\n")) # para saber que va ser el humano
turno_actual = elecc_humano #turno_actual se va encargar de cambiar los turnos
#donde meter el cambio de turno

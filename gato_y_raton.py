import random
tamano_x = 5    #tamano i de la matriz 
tamano_y = 5    #tamano j de la matriz
cant_turno = 5 #Para finalizar el juego
tablero = [] #tablero de juego
pos_gato = [] #posicion del gato
pos_raton = [] #posicion del raton

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
    for i in tablero:
        for j in i:
            print(" ",j,end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
        print(" ")

def colocar_personaje(personaje): #Posibles problemas, si el random hace que esten my cerca
    i = random.randint(0, tamano_x - 1) #genera un valor random para el eje x
    j = random.randint(0, tamano_y - 1) #genera un valor random para el eje y
    while tablero[i][j] != personaje: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero[i][j] == 0:
            tablero[i][j] = personaje
    return i,j   #retorna lo las posiciones

def fun_de_mov_human(gat_o_rat):
    mov = input(f"donde desdea mover? \nw - Arriba \ns - Abajo  \nd - Derecha \na - Izquierda\n")
   
    if movimineto_valido(mov, gat_o_rat): # movimiento valido que sea true or false
        mover_ficha(mov, gat_o_rat)
        pass
    elif mov == "s":
        pass
    elif mov == "d":
        pass
    elif mov == "a":
        pass
    else:
        pass
        print("")

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

def mover_ficha(mov, gat_o_rat): #Funcion funciona mal
    if gat_o_rat == 1:
        pos = pos_gato
    else:
        pos = pos_raton
    
    if mov == "w":
        tablero[pos[0]][pos[1]] = 0
        tablero[pos[0]-1][pos[1]] = gat_o_rat   
    if mov == "s":
        tablero[pos[0]][pos[1]] = 0
        tablero[pos[0]+1][pos[1]] = gat_o_rat   
    if mov == "d":
        tablero[pos[0]][pos[1]] = 0
        tablero[pos[0]][pos[1]+1] = gat_o_rat
    if mov == "a": 
        tablero[pos[0]][pos[1]] = 0
        tablero[pos[0]][pos[1]-1] = gat_o_rat   
    
def corroborar_fin():
    pass

print("Juego del gato y raton")
pos_gato = colocar_personaje(1)
pos_raton = colocar_personaje(2)
print(pos_gato,pos_raton)
imprimir_tablero()

gat_o_rat = int(input("Desea ser:\n1 : Gato \n2 : Raton\n")) # para saber que va ser el humano

while True:
    imprimir_tablero()
    fun_de_mov_human(gat_o_rat)
    corroborar_fin()

import random
tamano_x = 5    #tamano i de la matriz 
tamano_y = 5    #tamano j de la matriz
cant_turno = 5 #Para finalizar el juego
tablero = [] #tablero de juego
pos_gato = [] #posicion del gato
pos_raton = [] #posicion del raton

def crear_tablero(): #funcion que crea el tablero y lo llena de 0
   for fila in range(tamano_x):
       fila = []
       for columna in range(tamano_y):
           fila.append(0)
       tablero.append(fila)

def imprimir_tablero(): #funcion para imprimir el tablero, mas adelante, ver de imprimir con letras, o si es conveniente usar nomas letra
    for i in tablero:
       print(f"{i}\n")

def colocar_personaje(personaje): #Posibles problemas, si el random hace que esten my cerca
    i = random.randint(0, tamano_x - 1) #genera un valor random para el eje x
    j = random.randint(0, tamano_y - 1) #genera un valor random para el eje y
    while tablero[i][j] != personaje: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero[i][j] == 0:
            tablero[i][j] = personaje
    return i,j   #retorna lo las posiciones

crear_tablero()

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

def movimineto_valido(mov, gat_o_rat): #Corroborar si se puede mover a donde se quiere, da true o false, si el movimiento se puede o no hacer
    if gat_o_rat == 1:
        pos = pos_gato
    else:
        pos = pos_raton
    print(pos)

    if mov == "w":
        if (pos[0]-1) >= 0: #pos[0]-1 >= 0, se toma este valor para corroborar que no desborde por arriba
            return True
        else:
            return False
    elif mov == "s":
        if (pos[0] + 1) < tamano_x: #pos[0] + 1 <= tamano_x, para que no desborde por abajo 
            return True
        else:
            return False
    elif mov == "d":
        if (pos[1]+1) < tamano_y: #pos[1]+1 <= tamano_y, para que no desborde por la derecha
            return True
        else:
            return False
    elif mov == "a":
        if (pos[1]-1) >= 0: #pos[1]-1 <= 0, para que no desborde por la izquierda
            return True
        else:
            return False

def mover_ficha(mov, gat_o_rat): #Funcion todavia no funcion
    if gat_o_rat == 1:
        pos = pos_gato
    else:
        pos = pos_raton
    
    if mov == "w":

    if mov == "s":
    if mov == "d":
    if mov == "a": 
    
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

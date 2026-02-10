import random
tamano_x = 20
tamano_y = 20
tablero = []
cant_turno = 5 #Para finalizar el juego
pos_gato = []
pos_raton = []
#necesito guardar la posicion del gato y del raton en todo momento

def crear_tablero():
   for fila in range(tamano_x):
       fila = []
       for columna in range(tamano_y):
           fila.append(0)
       tablero.append(fila)

def imprimir_tablero():
    for i in tablero:
       print(f"{i}\n")

def colocar_personaje(personaje): #Posibles problemas, si el random hace que esten my cerca
    f = random.randint(0, tamano_x - 1)
    c = random.randint(0, tamano_y - 1)
    while tablero[f][c] != personaje:
        f = random.randint(0, tamano_x - 1)
        c = random.randint(0, tamano_y - 1)
        if tablero[f][c] == 0:
            tablero[f][c] = personaje
    return f,c

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
            print("TRUE", pos)
            return True
        else:
            print("FALSE")
            return False
    elif mov == "s":
        if (pos[0] + 1) < tamano_x: #pos[0] + 1 <= tamano_x, para que no desborde por abajo 
            print("TRUE", pos)
            return True
        else:
            print("FALSE")
            return False
    elif mov == "d":
        if (pos[1]+1) < tamano_y: #pos[1]+1 <= tamano_y, para que no desborde por la derecha
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False
    elif mov == "a":
        if (pos[1]-1) >= 0: #pos[1]-1 <= 0, para que no desborde por la izquierda
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False

def mover_ficha(mov, gat_o_rat): #Funcion todavia no funcion
    if gat_o_rat == 1:
        tablero[pos_gato[0]][pos_gato[1]]
       
    elif gat_o_rat == 2: # Raton
        tablero[pos_raton[0]][pos_raton[1]]
    pass

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

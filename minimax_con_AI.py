#CODIGO QUE FUNCIONA

import random

tamano_x = 5            #Tamano i de la matriz
tamano_y = 5            #Tamano j de la matriz
cant_turno = 10         #Cantidad de turnos

#entender bien random.choice y random.randint

#Se encarga de crear el tablero y llenarlo de "." y retornarlo
def crear_tablero():
    tablero = []
    for fila in range(tamano_x):
       fila = [] # Se crea una lista (fila) vacia
       for columna in range(tamano_y):  
           fila.append(".") # Se meten los "." en la fila 1 por 1
       tablero.append(fila) # Se agrega la fila a la matriz
    return tablero

#Imprime el tablero de manera estetica
def imprimir_tablero(tablero_de_juego):
    for i in tablero_de_juego:
        fila = " ".join(i)
        print(fila)

#Se encarga de poner al gato y al rato en el tablero al azar 
def colocar_personaje(personaje, tablero_de_juego):
    while True: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1) #randitn es la funcion del modulo random 
        if tablero_de_juego[i][j] == ".":
            tablero_de_juego[i][j] = personaje
            return i,j   #retorna lo las posiciones

#Imprime lo que serian los controles del humano y retorna el movimiento seleccionado
def fun_de_mov_human(mov):
    mov = input(f"Donde desdea mover:\n"
        "   w     \n"
        "a     d  \n"
        "   s     \n"
        "Elección: ")
    return mov

#Corrobora que el movimiento sea valido, que este dentro de la matriz
def movimineto_valido(mov, pos):
    i = pos[0]
    j = pos[1]

    if mov == "w":
        return (i - 1) >= 0 #pos[0]-1 >= 0, se toma este valor para corroborar que no desborde por arriba, retorna TRUE o False 
    elif mov == "s":
        return (i + 1) < tamano_x #pos[0] + 1 <= tamano_x, para que no desborde por abajo retorna TRUE o False 
    elif mov == "d":
        return (j + 1) < tamano_y #pos[1]+1 <= tamano_y, para que no desborde por la derecha retorna TRUE o False 
    elif mov == "a":
        return (j - 1) >= 0 #pos[1]-1 <= 0, para que no desborde por la izquierda retorna TRUE o False 
    else:
        return False      

#Se encarga de mover la ficha a su nueva posicion, y poner "." en el lugar donde estaba
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

#Se usa para la AI, de manera a ver las siguientes movidas
def mover_ficha_sim(mov, pos):
    i = pos[0]
    j = pos[1]

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1
    return i,j 

#Corrobora los casos posibles de fin del juego
def corroborar_fin(cant_turno, pos_1,  pos_2):
    if  cant_turno == 0:
        return True
    elif pos_1 == pos_2:  
        return True
    else:
        return False

#Da valores para que el minimax decida que hacer
def puntajes_minimax(pos_gato, pos_raton, profundidad):
    dist_manhatan =  abs(pos_gato[0]-pos_raton[0]) + abs(pos_gato[1]-pos_raton[1])
    
    if pos_gato == pos_raton:
        return float('inf') - (6 - profundidad) #hace que funcione mejor, castiga ligeramente las victorias lejanas
    else:
        return -dist_manhatan #Es heurisitica, porque le estas diciendo para donde ir, de manera a que termine el juego
    
#Cambia el turno
def cambiar_turno(turno_actual):
    if turno_actual == "G":
        turno_actual = "R"
    else:
        turno_actual = "G"
    return turno_actual

#Hace el minimax
def minimax(pos_gato, pos_raton, cant_turno, profundidad, maximizador):
    movimientos = ["w","s","a","d"]
    
    if profundidad == 0 or corroborar_fin(cant_turno, pos_gato, pos_raton):
        return puntajes_minimax(pos_gato, pos_raton, profundidad)

    if maximizador:
        maximo = -float('inf')
        for movimiento in movimientos:
            #Solo corrobora desbordamiento
            if movimineto_valido(movimiento, pos_gato):
                pos_gato_sim = list(mover_ficha_sim(movimiento, pos_gato))
                #le paso la posible juagada para que me de un valor y asi comparar ese valor con las otras posibles jugadas
                aux_max = minimax(pos_gato_sim, pos_raton, cant_turno - 1, profundidad - 1, False) 
                maximo = max(aux_max, maximo)
        return maximo
    else:
        minimo = float('inf')
        for movimiento in movimientos:
            if movimineto_valido(movimiento, pos_raton):
                pos_raton_sim = list(mover_ficha_sim(movimiento, pos_raton))
                #le paso la posible juagada para que me de un valor y asi comparar ese valor con las otras posibles jugadas
                aux_min = minimax(pos_gato, pos_raton_sim, cant_turno - 1, profundidad - 1, True)
                minimo = min(aux_min, minimo)
        return minimo

#La juagada de la IA 
#En casos particulares el raton se suicida, por la eleccion al azar si los resoltados de las posibles jugadas
#son iguales
def fun_de_mov_ai(turno_actual, pos_gato, pos_raton):
    movimientos = ["w","s","a","d"]
    mejores_mov = []
    profundidad = 6

    if turno_actual == "G":
        mejor_puntaje = -float('inf')
    else:
        mejor_puntaje = float('inf')

    if turno_actual == "G":
        for movimiento in movimientos:
            if movimineto_valido(movimiento, pos_gato):
                pos_gato_sim = list(mover_ficha_sim(movimiento, pos_gato))
                puntaje = minimax(pos_gato_sim, pos_raton, cant_turno - 1, profundidad - 1, False)
                print(puntaje)
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejores_mov = [movimiento] #se guarda con corchete para que guarde como una lista y 
                    #poder usar append y random, al igual que recetear la lista 
                
                elif puntaje == mejor_puntaje:
                    mejores_mov.append(movimiento)#Si los valores de las jugadas son iguales se 
                    #agregan a una lista
    else:
        for movimiento in movimientos:
            if movimineto_valido(movimiento, pos_raton):
                pos_raton_sim = list(mover_ficha_sim(movimiento, pos_raton))
                puntaje = minimax(pos_gato, pos_raton_sim, cant_turno - 1, profundidad - 1, True)
                print(puntaje)
                if puntaje < mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejores_mov = [movimiento]#se guarda con corchete para que guarde como una lista y 
                    #poder usar append y random, al igual que recetear la lista 
                
                elif puntaje == mejor_puntaje:
                    mejores_mov.append(movimiento)#Si los valores de las jugadas son iguales se 
                    #agregan a una lista

    if mejores_mov:
        return random.choice(mejores_mov)#en el caso de que solo haya 1 elemento, no se dieron igualdades arriba,
    #random.choice devuelve directamente la unica cosa que tiene dentro 

tablero_de_juego = crear_tablero()
print("Juego del Gato y Raton")
pos_gato = list(colocar_personaje("G",tablero_de_juego))
pos_raton = list(colocar_personaje("R",tablero_de_juego))
imprimir_tablero(tablero_de_juego)
#Selecciona el modo de juego
modo_de_juego = int(input("Que modo de juego desea elegir:\n1 : Humano (humano sera siempre Gato) vs IA \n2 : IA vs IA\nElección: "))
#Si se elige que el humano comience, siempre sera el Gato
if modo_de_juego == 1:
    ficha_jugador = "G"
    turno_actual = ficha_jugador
else:
    ficha_jugador = ""
    turno_actual = "G"

while True:
    imprimir_tablero(tablero_de_juego)
    if turno_actual == "G":
        print("Truno del Gato")
    else:
        print("Turno del Raton")
#Jugada de Humano 
    if turno_actual == ficha_jugador and modo_de_juego == 1:
        mov = fun_de_mov_human(ficha_jugador)
        if ficha_jugador == "G":
            if movimineto_valido(mov, pos_gato):
                pos_gato = list(mover_ficha(mov, "G", pos_gato,tablero_de_juego))
                cant_turno -= 1
                turno_actual = cambiar_turno(turno_actual)
                print(turno_actual)
            else:
                print("Ese movimiento no es valido")
#Jugada de IA
    else:
        #Se llama a la funcion que llama al minimax para la mejor jugada
        mov_ai = fun_de_mov_ai(turno_actual,pos_gato,pos_raton)
        #Solo hace la mejor jugada posible, que se devuelve en el fun_de_mov_ai
        if turno_actual == "G":
            pos_gato = list(mover_ficha(mov_ai, "G", pos_gato, tablero_de_juego))
        else:
            pos_raton = list(mover_ficha(mov_ai, "R", pos_raton, tablero_de_juego))
        cant_turno -= 1
        turno_actual = cambiar_turno(turno_actual)
#Corrobora fin de juego, se hace de esta manera para poder urilizar la funcion corroborar_fin en el minimax
    if corroborar_fin(cant_turno, pos_gato, pos_raton):
        if  pos_gato == pos_raton:
            tablero_de_juego[pos_gato[0]][pos_gato[1]] = "G"
            print("El GATO comio al raton")  
        elif cant_turno == 0:
             print("El RATON se escapo")    
        imprimir_tablero(tablero_de_juego)
        break
import random
import copy

#Variable globales
tamano_x = 5            #Tamano i de la matriz
tamano_y = 5            #Tamano j de la matriz
cant_turno = 50         #Para finalizar el juego
turno_actual = 0        #Elturno actual que se esta jugando
#nivel 1: la AI mueve al azar
#nivel 2: la AI es greedy, busca la mejor jugada sin ver a futuro
#nivel 3: la AI ya ve a futuro
nivel_ai = 0
tablero = []            #Tablero de juego
pos_gato = []           #Posicion del gato
pos_raton = []          #Posicion del raton

#Funcion que crea el tablero y lo llena de 0
def crear_tablero():
    for fila in range(tamano_x):
       fila = [] # Se crea una lista (fila) vacia
       for columna in range(tamano_y):  
           fila.append(0) # Se meten los 0 en la fila 1 por 1
       tablero.append(fila) # Se agrega la fila a la matriz

#Funcion para imprimir el tablero, mas adelante, ver de imprimir con letras,
#o si es conveniente usar nomas letra
def imprimir_tablero():
    for i in tablero:
        for j in i:
            print(" ",j,end="") #imprime de manera estetica la tabla, end sirve para que las lineas se impriman de manera horizontal
        print(" ")

#Esta funcion vaservir a modo que se vea estetico el juego el otro es solo para logica
def imprimir_tablero_estetico():
    for i in tablero:
        for j in i:
            if j == 0: print(" ",".",end="")
            elif j == 1: print(" ","G",end="") #al poner los emojis la matriz cambia, y ya no es estetica
            else: print(" ","R",end="")
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

#Se encarga de imprimir a donde desea mover el humano, y llamar a las funciones que
#corroboran el movimiento y que hace el movimiento
def fun_de_mov_human(elecc_humano):
#poner un if, si es gato mira solo 4 opciones de movimiento, si es raton mira 8
    if elecc_humano == 1:
        mov = input(f"Donde desdea mover:\n"
        "   w     \n"
        "a     d  \n"
        "   s     \n"
        "Elección: ")

    else:
        mov = input(f"Donde desdea mover:\n"
        "q  w  e  \n"
        "a     d  \n"
        "z  s  x  \n"
        "Elección: ")
   
    if movimineto_valido(mov, elecc_humano): #Si el movimiento es valido hace el movimiento
        mover_ficha(mov, elecc_humano)
        return True
    else:
        print("Ese movimiento no es valido")
        return False

#Todavia no es inteligente, pero ya puede mover
#nivel 1: la AI mueve al azar - TERMINADO, LOS 2 USAN LA MISMA LOGICA
#nivel 2: la AI es greedy, busca la mejor jugada sin ver a futuro - LAS LOGICAS YA DEBEN SER DIFERENTES
#nivel 3: la AI ya ve a futuro - LAS LOGICAS YA DEBEN SER DIFERENTES
def fun_de_mov_ai(elecc_humano):
    global nivel_ai
    if elecc_humano == 1:
        elecc_ai = 2
        mejor_distancia = 0
        movimientos = ["w","s","a","d","q","e","z","x"] #Se usa para elegir un moviemto aleatorio RATON
    else:
        elecc_ai = 1
        mejor_distancia = 999
        movimientos = ["w","s","a","d"] #Se usa para elegir un moviemto aleatorio GATO
    if nivel_ai == 1:
        while True:
#Elige un movimiento predeterminado que se definio en movimineto valido
            if elecc_ai == 1:
                mov = movimientos[random.randint(0, 3)]
            else:
                mov = movimientos[random.randint(0, 7)]
       
            if movimineto_valido(mov, elecc_ai):
                mover_ficha(mov,elecc_ai)
                break
#################### NIVEL 2 ############################
    elif nivel_ai == 2:
        for movidas in movimientos:
            if movimineto_valido(movidas, elecc_ai):
                if elecc_ai == 1:
                    i = pos_gato[0]
                    j = pos_gato[1]
                    sim_gato = list(mover_ficha_simulada(i,j,elecc_ai,movidas))
                    dist = calcular_distancia(sim_gato,elecc_ai)
                else:
                    i = pos_raton[0]
                    j = pos_raton[1]
                    sim_raton = list(mover_ficha_simulada(i,j,elecc_ai,movidas))
                    dist = calcular_distancia(sim_raton,elecc_ai)

def mover_ficha_simulada(i,j,elecc_ai,mov):
    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1
    elif elecc_ai == 2:#Mover fichas en diagonal SOLO RATON
        if mov == "q": #Diagonal izquierda, superior SOLO RATON
            i -= 1
            j -= 1
        elif mov == "e": #Diagonal derecha, superior SOLO RATON
            i -= 1
            j += 1
        elif mov == "z": #Diagonal izquierda, inferior SOLO RATON
            i += 1
            j -= 1
        elif mov == "x": #Diagonal derecha, inferior SOLO RATON
            i += 1
            j += 1

    if elecc_ai == 1: # guarda la nueva posicion de la ficha juagada
        return i,j
    else:
        return i,j
    
def calcular_distancia(posicion_sim, elecc_ai):
    if elecc_ai == 1:
        return abs(posicion_sim[0]-pos_raton[0]) + abs(posicion_sim[1]-pos_raton[1])
    else:
        return abs(posicion_sim[0]-pos_gato[0]) + abs(posicion_sim[1]-pos_gato[1])

#Cambia el turno
def cambiar_turno():
    global turno_actual
    if turno_actual == 1:
        turno_actual = 2
    else:
        turno_actual = 1

#Corroborar si se puede mover a donde se quiere, da true o false,
#si el movimiento se puede o no hacer
def movimineto_valido(mov, elecc_humano):
    if elecc_humano == 1:
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
    elif elecc_humano == 2: #Validacion de diagonales solo para el RATON
        if mov == "q":  #Diagonal izquierda, superior SOLO RATON
            return (i - 1) >= 0 and (j - 1) >= 0
        elif mov == "e": #Diagonal derecha, superior SOLO RATON
            return (i - 1) >= 0 and (j + 1) < tamano_y
        elif mov == "z": #Diagonal izquierda, inferior SOLO RATON
            return (i + 1) < tamano_x and (j - 1) >= 0
        elif mov == "x": #Diagonal derecha, inferior SOLO RATON
            return (i + 1) < tamano_x and (j + 1) < tamano_y
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
 #poner un if, si es gato mira solo 4 opciones de movimiento, si es raton mira 8

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1
    elif elecc_humano == 2:#Mover fichas en diagonal SOLO RATON
        if mov == "q": #Diagonal izquierda, superior SOLO RATON
            i -= 1
            j -= 1
        elif mov == "e": #Diagonal derecha, superior SOLO RATON
            i -= 1
            j += 1
        elif mov == "z": #Diagonal izquierda, inferior SOLO RATON
            i += 1
            j -= 1
        elif mov == "x": #Diagonal derecha, inferior SOLO RATON
            i += 1
            j += 1

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
        tablero[pos_gato[0]][pos_gato[1]] = 1
        print("El GATO comio al raton")        
        return True
    else:
        return False

############## NO SE COMO HACER MINIMAX #####################################
def caso_base():
    if corroborar_fin():
        pass
    if cant_turno == 0:
        pass

    pass

def evaluar_tablero(elecc_ai):
    pass

def minimax():
    pos_g_sim = pos_gato
    pos_r_sim = pos_raton
    dist_manh = abs(pos_g_sim[0]-pos_r_sim[0]) + abs(pos_g_sim[1]-pos_r_sim[1])
    if dist_manh:
        pass
    pass
####################################################


print("Juego del Gato y Raton")
crear_tablero()
#Se usa list() para que el valor que retorna sea una lista y no tupla
#hacer una funcion o en la misma de colocar personaje, que se encargue de que si estan muy cerca separe los personajes
pos_gato = list(colocar_personaje(1))
pos_raton = list(colocar_personaje(2))
imprimir_tablero_estetico()
#Para saber que va ser el humano
nivel_ai = int(input("Dificulad de la AI:\n1 : Nivel 1\n2 : Nivel 2\n3 : Nivel 3\nElección: "))
elecc_humano = int(input("Desea ser:\n1 : Gato \n2 : Raton\nElección: "))
#Turno_actual se va encargar de cambiar los turnos
turno_actual = elecc_humano
#Que pasa si piden que el comienzo del turno sea al azar, rand entre 1 o 2

while True:
    imprimir_tablero_estetico()
    #Humano
#Corroboramos que el turno sea del humano
    if turno_actual == elecc_humano:
        if elecc_humano == 1: titulo = "Gato"
        else: titulo = "Raton"
        print(f"Es el turno del {titulo}")
#Corrobora que la jugada se hizo para cambiar el turno, y llama a la funcion que mueve la pieza
        if fun_de_mov_human(elecc_humano):
            cant_turno -= 1 #Se pone en los 2, pero se podria poner solo en uno para que dure mas el juego
            cambiar_turno()
        if corroborar_fin():#Corrobora si el juego termina
            imprimir_tablero_estetico()
            break
    else:
    #Maquina
        if elecc_humano == 1: titulo = "Raton"
        else: titulo = "Gato"
        print(f"Es el turno del {titulo}")
        #funcion de AI #Hacer la funcion de la computadora
        fun_de_mov_ai(elecc_humano)
        cambiar_turno()
        if corroborar_fin():#Corrobora si el juego termina
            imprimir_tablero_estetico()
            break
    print(f"Faltan {cant_turno} para que el raton se escape")

#HAY UN ERROR DE FIN DE JUEGO, CORROBORAR DONDE SE IMPRIME LA CANTIDAD DE TURNOS
#crear limpiar pantalla, para mas adelante

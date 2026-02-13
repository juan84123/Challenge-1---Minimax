import random
import copy

#Variable globales
tamano_x = 5            #Tamano i de la matriz
tamano_y = 5            #Tamano j de la matriz
cant_turno = 50         #Para finalizar el juego
turno_actual = 0        #Elturno actual que se esta jugando
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
    while True: #si el valor en la matriz con los valores random son iguales
        i = random.randint(0, tamano_x - 1)
        j = random.randint(0, tamano_y - 1)
        if tablero[i][j] == 0:
            tablero[i][j] = personaje
            return i,j   #retorna lo las posiciones

#Se encarga de imprimir a donde desea mover el humano, y llamar a las funciones que
#corroboran el movimiento y que hace el movimiento
def fun_de_mov_human(elecc_humano):
#poner un if, si es gato mira solo 4 opciones de movimiento, si es raton mira 8
    mov = input(f"Donde desdea mover:\n"
        "   w     \n"
        "a     d  \n"
        "   s     \n"
        "Elección: ")

    if movimineto_valido(mov, elecc_humano): #Si el movimiento es valido hace el movimiento
        mover_ficha(mov, elecc_humano)
        return True
    else:
        print("Ese movimiento no es valido")
        return False

#Todavia no es inteligente, pero ya puede mover
def fun_de_mov_ai(elecc_humano):
    movimientos = ["w","s","a","d"]
    mejor_mov = []
    profundidad = 10

    if elecc_humano == 1:
        elecc_ai = 2 #La AI es el Raton
        mejor_valor = 9999 #Se pone el maximo para comparar y que el Rato busque el numero menor
    else:
        elecc_ai = 1 #La AI es el Gato
        mejor_valor = -9999 #Se pone el minimo para comparar y que el Gato busque el numero mayor

    for movimiento in movimientos:
        if movimineto_valido(movimiento,elecc_ai):
            #simula el primer movimiento
            if elecc_ai == 1:
                hijo = list(mover_ficha_simulada(movimiento, pos_gato, 1))
                valor = minimax(hijo, pos_raton, cant_turno, profundidad, False)
                # --- LÓGICA DE DESEMPATE PARA EL GATO (MAX) ---
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejores_movimientos = [movimiento] # Nuevo ganador único
                elif valor == mejor_valor:
                    mejores_movimientos.append(movimiento) # Empate, se suma a la lista
            else:
                hijo = list(mover_ficha_simulada(movimiento, pos_raton, 2))
                valor = minimax(pos_gato, hijo, cant_turno, profundidad, True)
                # --- LÓGICA DE DESEMPATE PARA EL RATÓN (MIN) ---
                if valor < mejor_valor:
                    mejor_valor = valor
                    mejores_movimientos = [movimiento] # Nuevo ganador único
                elif valor == mejor_valor:
                    mejores_movimientos.append(movimiento) # Empate, se suma a la lista
# Elección final: si hay opciones, elige una al azar entre las mejores
    if mejores_movimientos:
        mejor_mov = random.choice(mejores_movimientos)
        print(f"--- IA decide mover a: {mejor_mov} (opciones: {mejores_movimientos}) ---")
        mover_ficha(mejor_mov, elecc_ai)

def mover_ficha_simulada(mov,pos_a_evaluar,elecc_ai):
    i = pos_a_evaluar[0]
    j = pos_a_evaluar[1]

    if mov == "w": #Mueve las piezas, arriba
        i -= 1
    elif mov == "s": #Mueve las piezas, abajo
        i += 1
    elif mov == "d": #Mueve las piezas, derecha
        j += 1
    elif mov == "a": #Mueve las piezas, izquierda
        j -= 1

    if elecc_ai == 1: # guarda la nueva posicion de la ficha juagada
        return i,j
    else:
        return i,j

#Cambia el turno
def cambiar_turno():
    global turno_actual
    if turno_actual == 1:
        turno_actual = 2
    else:
        turno_actual = 1

#Corroborar si se puede mover a donde se quiere, da true o false,
#si el movimiento se puede o no hacer
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
    

def corroborar_fin_simulado(pos_g_sim,pos_r_sim,cant_turno,profundidad):
    if pos_g_sim == pos_r_sim:
        return 1000 - profundidad
    if cant_turno <= 0:
        return -1000 + profundidad
    return 0

def movimiento_valido_sim(mov, pos_a_validar):
        
    i = pos_a_validar[0]
    j = pos_a_validar[1]

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

############## MINIMAX #####################################
def minimax(pos_g_sim,pos_r_sim, cant_turno_sim, profundidad, maximizingPlayer):
    dist_manh = abs(pos_g_sim[0]-pos_r_sim[0]) + abs(pos_g_sim[1]-pos_r_sim[1])
    
    mov = ["w","s","a","d"] 
    
    resultado = corroborar_fin_simulado(pos_g_sim, pos_r_sim, cant_turno_sim, profundidad)#caso base
    
    if resultado != 0: 
        return resultado
    
    if profundidad == 0:
        return - dist_manh
    
    if maximizingPlayer: #Este if se encarga de cambiar la jugada maximizadora de la minimizadora
        mejor_valor = -9999
        for movimiento in mov:
            if movimiento_valido_sim(movimiento,pos_g_sim):
                hijo = list(mover_ficha_simulada(movimiento,pos_g_sim,1))
                eval = minimax(hijo, pos_r_sim,cant_turno_sim - 1, profundidad - 1, False)
                mejor_valor = max(mejor_valor,eval)
        return mejor_valor
    else:
        mejor_valor = 9999
        for movimiento in mov:
            if movimiento_valido_sim(movimiento,pos_r_sim):
                hijo = list(mover_ficha_simulada(movimiento,pos_r_sim,2))
                eval = minimax(pos_g_sim, hijo,cant_turno_sim - 1, profundidad - 1, True)
                mejor_valor = min(mejor_valor,eval)
        return mejor_valor
############################################################

print("Juego del Gato y Raton")
crear_tablero()
#Se usa list() para que el valor que retorna sea una lista y no tupla
#hacer una funcion o en la misma de colocar personaje, que se encargue de que si estan muy cerca separe los personajes
pos_gato = list(colocar_personaje(1))
pos_raton = list(colocar_personaje(2))
imprimir_tablero_estetico()
#Para saber que va ser el humano
elecc_humano = int(input("Desea ser:\n1 : Gato \n2 : Raton\nElección: "))
#Turno_actual se va encargar de cambiar los turnos
turno_actual = elecc_humano
#Que pasa si piden que el comienzo del turno sea al azar, rand entre 1 o 2


#Hacer AI vs AI
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
        cant_turno -= 1 #Se pone en los 2, pero se podria poner solo en uno para que dure mas el juego
        cambiar_turno()
        if corroborar_fin():#Corrobora si el juego termina
            imprimir_tablero_estetico()
            break
       
    print(f"Faltan {cant_turno} para que el raton se escape")

#!/usr/bin/env python3
"""Este módulo contiene el juego Battleship, en el que sólo participa un jugador,
el enemigo será el PC. El jugador tiene 10 barcos que ubica en su propio tablero 
de tamaño seleccionado. Ganará quien destruya todos los barcos del oponente.
El jugador escoge entre Heads o Tails para saber quien tuene el primer turno. 
La D representa un barco que ha sido destruido, 
mientras que una X representa un disparo fallido.
"""

import random


######################Generar tableros####################
# PC
def listaPc(size):
    """
    Genera la tabla para el PC que se utilizará para guardar la
    posición de los barcos, no se mostrará en pantalla
    Args:
        size (int): tamaño del tablero
    Returns:
        [list]: tablero del Pc
    """
    lista1 = []
    fila = []
    for i in range(size):
        for j in range(size):
            fila.append("O")
        lista1.append(fila)
        fila = []
    return lista1


def listaPj(size):
    """Genera la tabla para el Pj
    Args:
        size (int): tamaño del tablero
    Returns:
        [list]: tablero del Pj
    """
    lista2 = []
    fila = []
    for i in range(size):
        for j in range(size):
            fila.append("O")
        lista2.append(fila)
        fila = []
    return lista2


# Lista generada para pc
def listaPcInScreen(size):
    """
    Genera la tabla para el PC de respaldo para mostrar en pantalla,
    ocultado la posución de los barcos del Pc
    Args:
        size (int): tamaño del tablero
    Returns:
        [list]: tablero del Pc
    """
    lista3 = []
    fila = []
    for i in range(size):
        for j in range(size):
            fila.append("O")
        lista3.append(fila)
        fila = []
    return lista3


################Posición de Barcos PC########################


def barcosPc(size):
    """
    La función escoge una posición aleatoria de los barcos del PC
    Returns:
        [list]: lista de lista con la posición de los barcos del PC
    """
    registroBarcosPc = []
    coordenadas = []
    lista1 = listaPc(size)
    while len(registroBarcosPc) != 10:
        filaPc = random.randint(0, len(lista1) - 1)
        columnaPc = random.randint(0, len(lista1) - 1)
        coordenadas.append(filaPc)
        coordenadas.append(columnaPc)
        if not coordenadas in registroBarcosPc:
            registroBarcosPc.append(coordenadas)
            lista1[filaPc][columnaPc] = "B"
        coordenadas = []
    return lista1

##############Mostrar tableros en pantalla ####################


def showBoard(pjBoard, pcBoard, nombrejugador):
    """
    Está función muestra los tableros en pantalla
    Args:
        pjBoard ([list]): tablero del usuario
        pcBoard ([list]): tablero del Pc
        nombrejugador ([str]): nombre que ingresó el usuario en el menú
    """
    print("=========PC=========")
    for i in range(len(pcBoard)):
        for j in range(len(pcBoard)):
            print(pcBoard[i][j], end=" ")
        print()
    print("====================")
    if nombrejugador == "":
        print("=========PJ=========")
    else:
        print("=======", nombrejugador, "===========")
    for i in range(len(pjBoard)):
        for j in range(len(pjBoard)):
            print(pjBoard[i][j], end=" ")
        print()

############## Desarrollo del juego ###########################


def game(listaPcOculta, listaPcPantalla, ListaPJ, nombreJugador, flip):
    """
    Esta funcion contiene las reglas del juego, es decir el desarrollo

    Args:
        listaPcOculta (list): Lista con la posición de los barcos del Pc
        listaPcPantalla (list): Lista que se muestra al jugador sin 
                                la posición del los barcos enemigos
        ListaPJ (list): Lista con los barcos en la posición que ingresó el
                        usuario
        nombreJugador (str): nombre que ingresó el usuario en el menú
        flip (bool): valor que dice si pj acertó en la moneda
    """

    barcosPc = 10
    barcosPj = 10
    turnos = 0
    if flip == True:
        while barcosPc > 0 and barcosPj > 0:
            # Inputs
            # Mientras que el disparo sea algo distinto a "O"
            # tiene que solicitar de nuevo
            i = True
            k = True
            while k == True:
                while i == True:
                    try:
                        filaDisparoPJ = int(input("Fila para disparar: "))
                        if filaDisparoPJ > len(listaPcOculta) or filaDisparoPJ < 0:
                            print("Disparo invalido")
                        else:
                            i = False
                    except ValueError:
                        print("Disparo invalido")
                j = True
                while j == True:
                    try:
                        columnaDisparoPj = int(
                            input("Colunma para disparar :"))
                        if columnaDisparoPj > len(listaPcOculta) or columnaDisparoPj < 0:
                            print("Disparo invalido")
                        else:
                            j = False
                    except ValueError:
                        print("Disparo invalido")
                if listaPcPantalla[filaDisparoPJ][columnaDisparoPj] != "O":
                    print("Disparo invalido")
                else:
                    k = False

            # Verificar donde se disparó
            if listaPcOculta[filaDisparoPJ][columnaDisparoPj] == "B":
                print("Impacto")
                listaPcOculta[filaDisparoPJ][columnaDisparoPj] = "D"
                listaPcPantalla[filaDisparoPJ][columnaDisparoPj] = "D"
                barcosPc -= 1
                print("Barcos enemigos restantes:", barcosPc)
                turnos += 1
            elif listaPcOculta[filaDisparoPJ][columnaDisparoPj] == "O":
                print("Disparo fallado")
                listaPcOculta[filaDisparoPJ][columnaDisparoPj] = "X"
                listaPcPantalla[filaDisparoPJ][columnaDisparoPj] = "X"
            # Disparo Pc
            # filaDisparo del PC
            print()
            print("Disparo Pc:")
            fdPc = random.randint(0, len(ListaPJ) - 1)
            # Columna dispqaro Pc
            cdPc = random.randint(0, len(ListaPJ) - 1)
            while ListaPJ[fdPc][cdPc] != "O" and ListaPJ[fdPc][cdPc] != "B":
                fdPc = random.randint(0, len(ListaPJ) - 1)
                cdPc = random.randint(0, len(ListaPJ) - 1)
            if ListaPJ[fdPc][cdPc] == "B":
                print("Impacto Enemigo")
                ListaPJ[fdPc][cdPc] = "D"
                barcosPj -= 1
                print("Barcos restantes de Pj: ", barcosPj)
                turnos += 1
            elif ListaPJ[fdPc][cdPc] == "O":
                print("Disparo fallado")
                ListaPJ[fdPc][cdPc] = "X"
                turnos += 1
            showBoard(ListaPJ, listaPcPantalla, nombreJugador)

    else:
        while barcosPc > 0 and barcosPj > 0:
            print("Disparo Pc:")
            fdPc = random.randint(0, len(ListaPJ) - 1)
            # Columna dispqaro Pc
            cdPc = random.randint(0, len(ListaPJ) - 1)
            while ListaPJ[fdPc][cdPc] != "O" and ListaPJ[fdPc][cdPc] != "B":
                fdPc = random.randint(0, len(ListaPJ) - 1)
                cdPc = random.randint(0, len(ListaPJ) - 1)
            if ListaPJ[fdPc][cdPc] == "B":
                print("Impacto Enemigo")
                ListaPJ[fdPc][cdPc] = "D"
                barcosPj -= 1
                print("Barcos restantes de Pj: ", barcosPj)
                turnos += 1
            elif ListaPJ[fdPc][cdPc] == "O":
                print("Disparo fallado")
                ListaPJ[fdPc][cdPc] = "X"
                turnos += 1
            # Inputs
            # Mientras que el disparo sea algo distinto a "O"
            # tiene que solicitar de nuevo
            k = True
            while k == True:
                i = True
                while i == True:
                    try:
                        filaDisparoPJ = int(input("Fila para disparar: "))
                        if filaDisparoPJ > len(listaPcOculta) or filaDisparoPJ < 0:
                            print("Disparo invalido")
                        else:
                            i = False
                    except ValueError:
                        print("Disparo invalido")
                j = True
                while j == True:
                    try:
                        columnaDisparoPj = int(
                            input("Colunma para disparar :"))
                        if columnaDisparoPj > len(listaPcOculta) or columnaDisparoPj < 0:
                            print("Disparo invalido")
                        else:
                            j = False
                    except ValueError:
                        print("Disparo invalido")
                if listaPcPantalla[filaDisparoPJ][columnaDisparoPj] != "O":
                    print("Disparo invalido")
                else:
                    k = False
            if listaPcOculta[filaDisparoPJ][columnaDisparoPj] == "B":
                print("Impacto")
                listaPcOculta[filaDisparoPJ][columnaDisparoPj] = "D"
                listaPcPantalla[filaDisparoPJ][columnaDisparoPj] = "D"
                barcosPc -= 1
                print("Barcos enemigos restantes:", barcosPc)
                turnos += 1

            elif listaPcOculta[filaDisparoPJ][columnaDisparoPj] == "O":
                print("Disparo fallado")
                listaPcOculta[filaDisparoPJ][columnaDisparoPj] = "X"
                listaPcPantalla[filaDisparoPJ][columnaDisparoPj] = "X"
            showBoard(ListaPJ, listaPcPantalla, nombreJugador)

    if barcosPc == 0:
        if nombreJugador == "":
            print("Game over")
            print("Pj Won")
        else:
            print(nombreJugador, "Won")
        print("Turns: ", turnos)
    elif barcosPj == 0:
        print("Game over")
        print("Pc Won")
        print("Turns: ", turnos)
    input("Presiones Enter volver al menu principal")

###################### inicio del juego ######################
###################### Posición de barcos PJ##################


def inicio(nombreJugador):
    """
    Esta función se le solucita al usuario ubicar los barcos para 
    iniciar el desarrollo del juego 

    Args:
        nombreJugador ([str]): nombre del jugador que fue introducido 
        en el menu
    """
    # Flip
    flipCoin = input("Heads or Tails: ")
    opciones = ["Heads", "Tails"]
    randomFlip = opciones[random.randint(0, 1)]
    flip = False
    if flipCoin == randomFlip:
        flip = True
        print(randomFlip, " you start")
    else:
        print(randomFlip, " the PC start")

    # Chose board size
    flag = True
    while flag == True:
        try:

            boardSize = int(input("Chose board size (min: 5, max: 15): "))
            if boardSize < 5 or boardSize > 15:
                print("ERROR: Invalid Size")
            else:
                flag = False
        except ValueError:
            print("ERROR: Invalid Size")

    print()
    # Registro barcos
    registroBarcos = []
    coordenadas = []
    barcos = 10
    lista2 = listaPj(boardSize)
    print("Seleccione la posicíon de sus barcos")
    while len(registroBarcos) != 10:
        fila = int(input("Ingrese fila: "))
        columna = int(input("Ingrese Columna: "))

        # Verifica si el valor es valido
        if (fila < 0 or fila > len(lista2) - 1) or (columna < 0 or columna > len(lista2) - 1):
            print("Valor invalido, ingrese otro valor")
            flag = True
            while flag == True:
                fila = int(input("Ingrese fila: "))
                columna = int(input("Ingrese Columna: "))
                print()
                if (fila < 0 or fila > len(lista2) - 1) or (columna < 0 or columna > len(lista2) - 1):
                    print("Valor invalido, ingrese otro valor")
                else:
                    flag = False

        coordenadas.append(fila)
        coordenadas.append(columna)
        if not coordenadas in registroBarcos:
            registroBarcos.append(coordenadas)
            lista2[fila][columna] = "B"
            barcos -= 1
            print("Barcos restantes: ", barcos)
            print()
        elif coordenadas in registroBarcos:
            print("Valor ya ingresado, ingrese otro valor: ")
        coordenadas = []
    # Barcos del pc
    lista1Pantalla = listaPcInScreen(boardSize)
    listaPcOculta = barcosPc(boardSize)
    showBoard(lista2, lista1Pantalla, nombreJugador)
    game(listaPcOculta, lista1Pantalla, lista2, nombreJugador, flip)


def mainMenu():
    """
    Contiene el menú principal del juego en donde se introduce el nombre
    o simplemente se inicia o se cierra 
    """
    opcion = 0
    nombreJugador = ""
    while opcion != 3:
        print("----- Los_Bachatines-----")
        print("------Batalla naval-----")
        print("------Menú  principal---")
        print()
        print("1. Introducir nombre del jugador")
        print("2. Iniciar juego")
        print("3. Cerrar programa.")
        try:
            opcion = int(input("Seleccione opción: "))
        except ValueError:
            print()

        if opcion == 1:
            nombreJugador = input("ingrese nombre: ")
            print("Hola", nombreJugador)
            print()
        elif opcion == 2:
            inicio(nombreJugador)
        elif opcion == 3:
            print("Fin del Programa")
        else:
            print("ERROR: seleción invalida")


mainMenu()

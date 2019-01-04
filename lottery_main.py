#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def desea_salir(texto):
    if texto == "q" or texto == "Q":
        return True
    else:
        return False


def repetimos(texto):
    if texto == "S":
        return True
    elif texto == "N":
        return False
    else:
        return None


def es_un_numero(numero):
    lo_es = None
    try:
        numero = int(numero)
        lo_es = True
    except ValueError:
        lo_es = False
    return lo_es


def desea_repertir():
    print

    no_es_correcta = True
    while no_es_correcta:
        op = raw_input("¿Desea repetir ('s/S'o 'n/N'): ")
        op = op.upper()[0]
        if repetimos(op) == None:
            if desea_salir(op):
                print "\nSaliendo de la aplicación..."
                no_es_correcta = False
                raw_input("Pulse una tecla.")
            else:
                print "\nLa opcion elegida no es correcta."
        else:
            no_es_correcta = False

    return repetimos(op)


def muestra_menu_inicial():
    print
    print "\n  Esto es un Juego de la Lotería que no te hará ganar pero śi te hará creertelo!! JAJAJAJA!!"
    print "----------------------------------------------------------------------------------------------\n"
    print "Menú:"
    print "1.-Bonoloto."
    print "2.-Primitiva."
    print "3.-Euromillones."
    print "4.-Personalizado."

    op_correcta = True
    while op_correcta:
        es_un_texto = False
        op = raw_input("Elige opción ('q/Q' para salir): ")
        if not desea_salir(op[0]):
            if es_un_numero(op):
                op = int(op)
            else:
                print "\nSeleccione un valor válido."
                es_un_texto = True

            if op > 0 and op < 5:
                op_correcta = False
            else:
                if not es_un_texto:
                    print "\nOpción elegida es incorrecta."
        else:
            op_correcta = False
            op = 0
    return op


def primitiva_y_bonoloto(tipo):
    # Tipo: 1=Bonoloto; 2=Primitiva
    #
    # Caracteristicas comunes:
    # Seis numeros del 1 al 49 y el reintegro del 0 al 9
    #####################################################

    tipo_sorteo = ["Bonoloto", "Primitiva"]
    tipo_seleccionado = tipo - 1

    nombre = None
    list_num = []
    primi = []

    for i in range(1, 49):
        list_num.append(i)
        primi.append(i)
    list_num.sort()
    primi.sort()

    nombre = tipo_sorteo[tipo_seleccionado]
    print "\n{}: ".format(nombre)

    comprobracion = []
    testigo = True
    while testigo:
        if len(primi) > 6:
            numerete = randint(1, 49)
            try:
                primi.remove(numerete)
            except ValueError:
                comprobracion.append(numerete)
        else:
            testigo = False

    comprobracion.sort()

    print "\nNúmeros: "
    #x = 1
    for element in primi:
        print ".-{}".format(element)#x, element)
        #x += 1

    print "\nReintegro: "
    print ".-{}".format(randint(0, 9))


def euromillones(tipo):
    # Tipo: 3=Euromillones
    #
    # Caracteristicas:
    # .-Cinco números entre 50 distintos y 2 estrellas entre 11 distintas.
    #######################################################################
    tipo_sorteo = "Euromillones"
    euromillones = []
    estrellas = []
    comprobar = []
    for i in range(1, 50):
        euromillones.append(i)
    euromillones.sort()

    for i in range(1, 11):
        estrellas.append(i)
    estrellas.sort()

    print "\n{}: ".format(tipo_sorteo)
    testigo = True
    while testigo:
        if len(euromillones) > 5:
            numero_aleatorio = randint(1, 50)
            try:
                euromillones.remove(numero_aleatorio)
            except ValueError:
                comprobar.append(numero_aleatorio)
        else:
            testigo = False

    testigo = True
    while testigo:
        if len(estrellas) > 2:
            numero_aleatorio = randint(1, 11)
            try:
                estrellas.remove(numero_aleatorio)
            except ValueError:
                comprobar.append(numero_aleatorio)
        else:
            testigo = False

    print "\nNúmeros: "
    x = 1
    for element in euromillones:
        print "{}.-{}".format(x, element)
        x += 1

    print "\nEstrellas: "
    x = 1
    for element in estrellas:
        print "{}.-{}".format(x, element)
        x += 1


def personalizado():
    print
    print "\nLotería Personalizada: "
    vamos_bien = True
    quiero_salir = False
    doble_numeros = None
    while vamos_bien:
        cantidad_numeros = raw_input("Introduzca la cantidad de numeros que desea que se generen aleatoriamente ('q/Q' para salir): ")
        if es_un_numero(cantidad_numeros):
            cantidad_numeros = int(cantidad_numeros)
            if cantidad_numeros < 50:
                doble_numeros = cantidad_numeros * ((100/7)*2)
            else:
                doble_numeros = cantidad_numeros * ((200/9)/2)
            vamos_bien = False
            print "Se generarán {} números de {} números aleatorios.".format(cantidad_numeros, doble_numeros)
        elif desea_salir(cantidad_numeros):
            raw_input("Saliendo del programa... Pulse una tecla.")
            vamos_bien = False
            quiero_salir = True
        else:
            print "Error al introducir el número."

    if not quiero_salir:
        numeros = []
        personalizar = []
        for i in range(1, doble_numeros):
            numeros.append(i)
        numeros.sort()

        testigo = True
        #x=1
        while testigo:
            if len(numeros) > cantidad_numeros:
                numeros_aleatorios = randint(1, doble_numeros)
                try:
                    numeros.remove(numeros_aleatorios)
                except ValueError:
                    #print "{}.-Numero repetido ({}).".format(x, numeros_aleatorios)
                    #x += 1
                    personalizar.append(numeros_aleatorios)
            else:
                testigo = False

        personalizar.sort()

        print "\nNúmeros generados aleatoriamente: "
        y = 1
        for element in numeros:
            print "{}.-{}".format(y, element)
            y += 1

#        print "\nY estos números han salido repetido: "
#        x = 1
#        for element in personalizar:
#            print "{}.-{}".format(x, element)
#            x += 1

#        print "\nVeamos otra manera de sacar los numero repetidos con la funcion 'Count()': "
#        print "\nVeamos primero la lista completa: "
#        print "\n{}".format(personalizar)
#        for i in range(1, doble_numeros):
#            print "El numero {} ha salido {} veces repetido.".format(i, personalizar.count(i))

    return quiero_salir


def main():
    no_salir = True
    testigo = False
    while no_salir:
        option = muestra_menu_inicial()
        if not option == 0:
            if option == 1 or option == 2:
                primitiva_y_bonoloto(option)
            elif option == 3:
                euromillones(option)
            elif option == 4:
                if personalizado():
                    testigo = True

            if testigo:
                no_salir = False
            else:
                if not desea_repertir():
                    no_salir = False

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()


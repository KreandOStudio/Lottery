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


def desea_repertir():
    print

    no_es_correcta = True
    while no_es_correcta:
        op = raw_input("¿Desea repetir ('s/S'o 'n/N'): ")
        op = op.upper()[0]
        if repetimos(op) == None:
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
            try:
                op = int(op)
            except ValueError:
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


def main():
    no_salir = True
    while no_salir:
        option = muestra_menu_inicial()
        if not option == 0:
            if option == 1 or option == 2:
                primitiva_y_bonoloto(option)
            elif option == 3:
                euromillones(option)

            if not desea_repertir():
                no_salir = False

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()


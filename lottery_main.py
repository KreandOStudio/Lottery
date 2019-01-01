#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def desea_salir(texto):
    if texto == "q" or texto == "Q":
        return True
    else:
        return False


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


def bonoloto_y_primitiva(tipo):
    # Tipo: 1=Bonoloto; 2=Primitiva
    #
    # Caracteristicas comunes:
    # Seis numeros del 1 al 49 y el reintegro del 0 al 9
    tipo_sorteo = ["Bonoloto", "Primitiva"]
    sorteo = []
    reintegro = None
    tipo = tipo - 1

    print
    print "Usted ha elegido el Sorteo de la {}.\n".format(tipo_sorteo[tipo])
    print "Esta es su combinación ganadora: "
    for i in range(1, 8):
        if i == 7: #Reintegro:
            reintegro = randint(0, 9)
        else:
            sorteo.append(randint(1, 49))

    sorteo.sort()

    x = 0
    for element in sorteo:
        print ".-{}".format(element)

    print "R.: {}".format(reintegro)
    print

    print "Ahora vamos a comprobar si funciona la funcion de comprobar si hay algun elemento repetido ('es_repetido(list)'): "
    print
    es_repetido(sorteo)


def es_repetido(list):
    numeroi = None
    list.sort()
    x = 0
    for i in range(x, len(list)):
        numeroi = list[i]
        no_es_igual = True
        y = x + 1
        while no_es_igual:
            if not y >= len(list):
                comprobar = list[y]
                if comprobar == numeroi:
                    print "En en puesto {} de la lista, es igual al numero {} en el puesto {}".format(numeroi, comprobar, y)
                    no_es_igual = False
                else:
                    print "El numero {} de la lista, no es igual al numero {} en el puesto {}.".format(numeroi, comprobar, y)
                    y += 1
            else:
                print "Salimos del bucle"
                no_es_igual = False
                x += 1


def main():
    no_es_correcto = True
    quiero_salir = False
    numero = None
    lista_de_numeros = []

    opcion = muestra_menu_inicial()
    if not opcion == 0:
        if opcion == 1:
            bonoloto_y_primitiva(opcion)
        elif opcion == 2:
            bonoloto_y_primitiva(opcion)

        while no_es_correcto:
            usuario = raw_input("Introduzca la cantidad de numeros que se generaran (del 1 al 100)('q/Q' para salir): ")
            try:
                numero = int(usuario)
                no_es_correcto = False
            except ValueError:
                if desea_salir(usuario.upper()[0]):
                    no_es_correcto = False
                    quiero_salir = True
                else:
                    print "\nError! En la lotería solo se usan números! Gracias!"
                    raw_input("Pulse una tecla para continuar.")

        if quiero_salir:
            print "Adeu!!"
        else:
            print "\nSe generarán {} números aleatorios y son estos:".format(numero)

            for i in range(1, numero+1):
                if i>1:
                    testigo = True
                    while testigo:
                        un_numero = randint(1, numero)
                        if not es_repetido(un_numero, lista_de_numeros):
                            lista_de_numeros.append(un_numero)
                            testigo = False
                        else:
                            print "\nEl numero generado es repetido. Se generará otro."
                else:
                    lista_de_numeros.append(randint(1, numero))

            lista_de_numeros.sort()
            x = 1
            for element in lista_de_numeros:
                print "Elemento {}, Numero {}".format(x, element)
                #x = x + 1
                x += 1
    else:
        print "\nGracias por usar Lottery."
        raw_input("Pulse una tecla para continuar.")
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()


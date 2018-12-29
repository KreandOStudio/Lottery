#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

no_es_correcto = True
quiero_salir = False
numero = None
lista_de_numeros = []

def desea_salir(texto):
    if texto == "q" or texto == "Q":
        return True
    else:
        return False

print "\n  Esto es un Juego de la Lotería que no te hará ganar pero śi te hará creertelo!! JAJAJAJA!!"
print "----------------------------------------------------------------------------------------------\n"

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


if quiero_salir:
    print "Adeu!!"
else:
    print "\nSe generarán {} números aleatorios y son estos:".format(numero)

    for i in range(1, numero+1):
        lista_de_numeros.append(randint(1, numero))

    x = 1
    for element in lista_de_numeros:
        print "Elemento {}, Numero {}".format(x, element)
        x = x + 1
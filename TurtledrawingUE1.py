from turtle import *
import random

reset()


def quadrat():
    pencolor('#001eff')
    fillcolor("orange")
    width(5)
    for i in range(4):
        forward(100)
        left(90)
    bye()


def dreieck():
    pencolor('#bd00ff')
    fillcolor("pink")
    width(22)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    bye()


def fünfeck():
    pencolor('#00b8ff')
    fillcolor("magenta")
    width(10)
    right(90)
    for i in range(0, 5):
        forward(100);
        left(72)
    bye()


def sechseck():
    pencolor('#d600ff')
    fillcolor("green")
    width(200)
    right(90)
    for i in range(0, 6):
        forward(100)
        left(60)
    bye()


formen = [quadrat(), sechseck(), fünfeck(), dreieck()] # weiß nicht warum die Funkton am Anfang immer sofort aufgerufen wird und damit die random Auswahl ned geht...
x = random.choice(formen)
x
# -*- coding: utf-8 -*-
#11. Hacer un programa que muestre un menú al usuario con las siguientes pizzas:
#1) Personal
#2) Mediana
#3) Grande
#4) Gorila
#Hacer una función que de acuerdo al número regrese el costo de la pizza que sería 40 para la personal, 80 para la mediana, 180 para la grande y 400 para la gorilla. Hacer que el programa también pregunte al usuario cuántas pizzas quiere y calcule el costo total.
#programado por Diego Silva y Favela
#Vea como pusimos el titulo, esta muy enriquecedor aparte que el nombre esta bien padre! por cierto, en la parte de el else, no pudimos como hacerle para que se regresara a que intentara poner denuevo el tipo de pizza
def pizza(tipo):
    if tipo==1:
        return 40
    elif tipo==2:
        return 80
    elif tipo==3:
        return 180
    elif tipo==4:
        return 400
    else:
        return "... espera, esa pizza no existe, estas bien @$%#!"

tipo=int(input(".:PIZZERIA MARV-O:.\nQue pizza quierre morro!?\n 1) Personal\n 2) Mediana\n 3) Grande\n 4) Gorila\n"))
print("Esa pizza  cuesta %s$" % pizza(tipo))
cuant=int(input("Muy bien morro, ahora cuantas de esas quiere? "))
cuant=cuant*pizza(tipo) #aqui multiplicamos el numero de pizzas por la funcion(el costo de la pizza)
print("OK men, son %s marv-O dollares..." % cuant)

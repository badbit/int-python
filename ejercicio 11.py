#coding=utf-8
#Programado por Navit Cardoso
#Programa de menu pizzas

x=int(input("Algo:"))
print("Programa que despliega un menu de pizzas y calcula el costo de una orden")

pizza=int(input("Selecccione una pizza:  1)Personal  2)Mediana  3)Grande  4)Gorila  Numero de pizza: "))


if pizza==1:
    pizza=40
    print("La pizza personal cuesta 40 pesos")
elif pizza==2:
    pizza=80
    print("La pizza mediana cuesta 80 pesos")
elif pizza==3:
    pizza=180
    print("La pizza grande cuesta 180 pesos")
elif pizza==4:
    pizza=400
    print("La pizza gorila cuesta 400 pesos")

cantidad=int(input("Cantidad de pizzas: "))
total=cantidad*pizza

print("Precio total: ", total)

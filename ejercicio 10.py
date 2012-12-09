#coding=utf-8
#Programado por Navit Cardoso
#Programa que obtiene el area de un poligono

print("Programa que obtiene el area de un poligono de n lados")
lado=int(input("Longitud de un lado: "))
numeroLados=int(input("Numero de lados: "))
apotema=int(input("Valor del apotema: "))
area=lado*numeroLados*apotema/2
print("Area del poligono: ", area)

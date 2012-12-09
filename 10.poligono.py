# -*- coding: utf-8 -*-
#programa que calcula el área de cualquier polígono regular.
#10 de octubre 2012
#programado por Diego Favela y Karina Lopez
def poligono(apotema, lado, lados):
    area=apotema*lado*lados/2
#aqui se efectua toda la operacion.
    return  area

print("Programa que calcula el area de un poligono.\n")
apotema= int(input("Introduce el valor del apotema: "))
lado= int(input("Introduce la medida del lado: "))
lados= int(input("Introduce el número de lados: "))
if lados<3:
    print("No hay tal cosa como polígonos de %s lados" %lados)
#por si alguien pone un "poligono" de 2 o menos lados.
else:
    print("El área del polígono es %s " %poligono(apotema,lado, lados))
#aqui ya presento la informacion.

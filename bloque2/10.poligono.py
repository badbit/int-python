# -*- coding: utf-8 -*-
# Programa que calcula el área de cualquier polígono regular mediante una función.
# Programado por Miguel Lozano.

def poligono(apotema, lado, lados):
    area = apotema*lado*lados/2
    return area

# Imprimir el mensaje de bienvenida.
print("Programa que calcula el area de un poligono.\n")

# Solicitar los datos requeridos.
apotema= int(input("Introduce el valor del apotema: "))
lado= int(input("Introduce la medida del lado: "))
lados= int(input("Introduce el número de lados: "))

# Verificar que el usuario haya solicitado el área de una figura de tres
#    o más lados.
if lados<3:
    print("No hay tal cosa como polígonos de %s lados" %lados)
else:
    print("El área del polígono es %s." % poligono(apotema,lado,lados))

#programa para calcular el �rea de cualquier poligono usando funciones
#10/10/12
#Programado por Luis Carlos Salgado
def area(lado,odal,apot):
   if odal<2:
   print("Polígono Inexistente")
else:
   perim=lado*odal
   ar=(perim*apot)/2
odal=int(input("¿Cuántos lados tiene su polígono?"))
apot=int(input("¿Cuánto mide su apotema"))
lado=int(input("¿Cuánto mide su lado"))
print("El área de su poligono es de %s unidades cuadradas") %area(lado,odal,apot)
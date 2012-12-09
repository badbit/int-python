#programa para area de poligono regular
print("programa para el area de un poligono regular ")
l=int(input("introduce el numero de lados "))
ml=int(input("introduce la medida de los lados "))
a=int(input("intoduce el apotema "))
if l<3:
    print("los poligonos tienen + de 2 lados")
else: p=ml*l
area=p*a/2
print("el area es %s" % area)

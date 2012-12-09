#coding=utf-8 
#programa que obtenga el area de cualquier poligono regular dados el apotema, el número de lados y la medida del lado.
#programado por: Benjamín, Paulina e Ian aka "los wachiturros"
#fecha: 28 de septiembre del 2012
def poligonoRegular(lado, apotema, numlados):
	if numlados<3: 
		return 0
	else:
		return lado*numlados*apotema/2
	print("el area del poligonoRegular es %S, el apotema es %S, el numlados es %S." %(lado, apotema, numlados))
	
lado= int(input("Introduce el valor del lado: "))
apotema= int(input("Introduce el valor del apotema: "))
numlados= int(input("Introduce el numlados: "))

print(poligonoRegular(lado, apotema, numlados))
	

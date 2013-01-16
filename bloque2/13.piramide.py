#coding=utf-8
# Programa que, dado un número de líneas,
#programado por: Diego Favela

def piramide(escalon):
	numero=1 #contador para parar el ciclo.
	carac=1 #numero de caracteres que se escriben en cada renglon.
	espa=escalon #numero de espacios para centrar la piramide
	while numero<=escalon:
		print("%s%s" %(espa*" ", carac*"A"))
		espa=espa-1
		carac=carac+2
		numero=numero+1
	print("\nAhi esta su piramide.")

print(".:Programa para crear una piramide:.")
escalon=int(input("Introduce el numero de escalones: "))
print("%s" %piramide(escalon))

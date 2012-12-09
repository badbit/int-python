#coding=utf-8
#12/10/2012
#programado por: Jose Enrique y Nayeli Reyes

def piramide(escalones):
	numero=1 
	asteriscos=1 
	espacios=escalones 
	while numero<=escalones:
		print("%s%s" %(espacios*" ", asteriscos*"*"))
		espacios=espacios-1
		asteriscos=asteriscos+2
		numero=numero+1
	print("\nMagnifica.")

print(".:Programa para crear una piramide:.")
escalones=int(input("Introduce el numero de escalones: "))
print("%s" %piramide(escalones))

#coding = utf-8
#Programa para saber el costo de una pizza mediente un menu
#Programado por Andrea Hernandez y Rossy Marmolejo
#28 de Septiembre

def persona(nombre, edad):
    if edad<18:
        print("Hola soy %s y soy menor de edad"%persona(nombre, edad)) 	
    else: 
	    print("Hola soy %s y soy mayor de edad"%persona(nombre, edad))

nombre= input("Introduce tu nombre:")
edad= input("Introduce tu edad:")
	

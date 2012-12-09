#coding= utf-8
#Programa que imprime si la persona es mayor de edad o no
#Programado por Bethania Vásquez


def persona(nombre, edad):
	if edad<18:
		mayoria = "menor"
	else:
		mayoria = "mayor"

	print("Mi nombre es %s y soy %s de edad." % (nombre, mayoria))

persona("Miguel", 29 )
persona("Rossy", 16 )

nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad")

persona(nombre, edad)

#coding: utf-8 
#Hacer un programa que muestre un menú al usuario con las siguientes pizzas:
#1) Personal
#2) Mediana
#3) Grande
#4) Gorila
#programado por benjamín, Paulina y josé.
#19/10/2012

def imprimirOrden(pedido):
	contador=0
	costo=0
	while contador<4:
		if contador==0:
			print ("cantidad de pizzas chicas")
		elif contador==1:
			print ("cantidad de pizzas medianas")
		elif contador==2:
			print ("cantidad de pizzas grandes")
		elif contador==3:
			print ("cantidad de pizzas gorilas")
		print(pedido[contador])
		costo+=pizza(contador)*pedido[contador]
		contador+=1
	print("EL costo total es %s" % costo)
		
		
def pizza(numero_de_pizza):
    if numero_de_pizza==0:
        return 40
    elif numero_de_pizza==1:
        return 80
    elif numero_de_pizza==2:
        return 180
    elif numero_de_pizza==3:
        return 400
    else:
        print("no existe tal pizza") 

pedido= [0,0,0,0]
tipo=0

print("""Bienvenido

1. Personal
2. Mediana
3. Grande
4. Gorila
5. Terminar orden""")


while tipo<5:
    tipo=int(input("Introduzca el tipo de pizza: "))
    if tipo!=5:
        cantidad= int(input("Introduzca cuantas pizzas de esas quieres:"))
        pedido[tipo-1]=pedido[tipo-1]+cantidad

imprimirOrden(pedido)



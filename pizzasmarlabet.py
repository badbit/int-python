#coding: utf-8 
#Programado por Marla Yépiz y Bethania Vásquez.
#Programa que muestre un menú de estas pizzas:
#1. Chica
#2. Mediana
#3. Grande
#4. Gorila

def imprimirorden(pedido):
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
	print("el costo total es %s" % costo)
		
		
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

print("""bienvenido

1. chica
2. mediana
3. grande
4. gorila
5. terminar orden""")


while tipo<5:
    tipo=int(input("Introduzca el tipo de pizza: "))
    if tipo!=5:
        cantidad= int(input("Introduzca cuantas pizzas de esas quieres:"))
        pedido[tipo-1]=pedido[tipo-1]+cantidad

imprimirOrden(pedido)




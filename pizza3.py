#coding = utf-8
#Programa para saber el costo de una pizza mediente un menu
#Programado por Andrea Hernandez y Rossy Marmolejo
#23 de octubre 2012

def imprimirOrden(orden):
	contador=0
	costo=0
	while contador<4:
		if contador==0:
			print("cantidad de pizza chicas")
		elif contador == 1:
			print("cantidad de pizza medianas")
		elif contador == 2:
			print("cantidad de pizza grandes")
		elif contador == 3:
			print("cantidad de pizza gorila")
		print(orden[contador])
		costo+=pizza(contador)*orden[contador]
		contador+=1
	print("El costo total es %s" % costo)
              
def pizza(tipo):
    if tipo == 0:
        return 40
    elif tipo == 1:
        return 100
    elif tipo == 2:
        return 180
    elif tipo == 3:	
	    return 450
    else:
     print("No tenemos esa opcion en el menu") 

pedido=[0,0,0,0]
tipo=0

print(""" MENU DE PIZZA
1 Personal 
2 Mediana  
3 Grande   
4 Gorila
5 Terminar orden""")

while tipo<5:
	tipo= int(input("Introduce tipo de pizza: "))
	if tipo!=5:
		cantidad= int(input("Introduce cuantas pizzas de ese tipo quieres:"))
		pedido[tipo-1]=pedido[tipo-1]+cantidad

imprimirOrden(pedido)

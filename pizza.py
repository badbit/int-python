#coding=utf-8
#programa para pizza
#programado por paulina aguilar
#10/17/2012

def pizza(tipo):
    if tipo == 1:
        return 40
    elif tipo == 2:
        return 100
    elif tipo == 3:
        return 180
    elif tipo == 4:	
	    return 450
    else:
     print("No tenemos esa opcion en el menu") 

print(""" MENU
1 Personal 
2 Mediana  
3 Grande   
4 Gorila""")

tipo= int(input("Introduce tipo de pizza:"))
cantidad= int(input("Introduce cuantas pizzas de ese tipo quieres:"))
print("El costo es de %s"% (pizza(tipo)*cantidad))

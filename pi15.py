# coding=utf-8
# Programado por: Diego Favela y Diego Silva.
# Programa que hace cosas con la pizza.
def pizza(orden, pizzun):
 i=0
 for tipos in pizzun:
   orden[i]=int(input("Cuantas pizzas %s quiere? " % tipos))
   if i==0:
    suma[i]=orden[i]*40
   elif i==1:
    suma[i]=orden[i]*80
   elif i==2:
    suma[i]=orden[i]*180
   elif i==3:
    suma[i]=orden[i]*400
   i+=1

def orfin(orden, pizzun):
 i=0
 for tipos in pizzun:
  print("Usted pidio %s pizza(s) %s, con un total de %s$" % (orden[i], tipos, suma[i]))
  i+=1
 sumatot=suma[0]+suma[1]+suma[2]+suma[3]
 print("\nEn total serian %s$" % sumatot)

print("Bienvenido a la pizzeria electronica!")
pizzun=["chicas", "medianas", "grandes", "gorilla"] #los nombres de las pizzas para ahorrar espacio
orden=[0, 0, 0, 0]
suma=[0, 0, 0, 0]
pizza(orden, pizzun)
orfin(orden, pizzun)

#coding=utf-8
#programado por: Diego Favela y Benjamin Salazar
#domingo 14 de octubre 2012
def pizza(tipo):
 suma=0 #numerador que suma las pizzas
 while 0<tipo<5:
  if tipo==1:
   suma=suma+40
   tipo=int(input("Okey, cual otra?\n"))
  elif tipo==2:
   suma=suma+80
   tipo=int(input("Okey, cual otra?\n"))
  elif tipo==3:
   suma=suma+180
   tipo=int(input("Okey, cual otra?\n"))
  elif tipo==4:
   suma=suma+400
   tipo=int(input("Okey, cual otra?\n"))
 print("Todas estas pizzas costaran %s$" %suma)

tipo=int(input("PIZZERIA DON BIPULINAR \nBienvenido a esta super pizzeria ¿qué desea ordenar?\n 1) Personal\n 2) Mediana\n 3) Grande\n 4) Gorila\n -Cualquier otro numero termina la orden\n"))
pizza(tipo) #el mensaje esta dentro de la funcion por que no pudimos hacelo con return

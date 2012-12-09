#def pedido(orden):
#    for tipo in orden:
#        tipo=int(input("que tipo de pizza quiere? "))
#        for cantidad in tipo:
#            if tipo==1:
#                cantidad=int(input("cuantas pizzas personales quiere?"))
#            elif tipo==2:
#                cantidad=int(input("cuantas pizzas medianas quiere?"))
#            elif tipo==3:
#                cantidad=int(input("cuantas pizzas grandes quiere?"))
#            elif tipo==4:
#                cantidad=int(input("cuantas pizzas gorillas quiere?"))

def pizza(orden):
    for tipo in orden:
		
        for cantidad in tipo:
            if tipo==1:
                print("pizzas personales:")
            elif tipo==2:
                print("pizzas medianas:")
            elif tipo==3:
                print("pizzas grandes:")
            elif tipo==4:
                print("pizzas gorillas:")
            print(cantidad)

orden=[[1,0],
       [2,0],
       [3,0],
       [4,0]]
pizza(orden)

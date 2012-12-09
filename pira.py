#progama para hacer una piramide


def piramide (escalon): 
     numero= 1
     estrellitas= 1
     espacio= escalon
     while numero<=escalon:
         print("%s%s" %(espacio*" ", estrellitas *"*"))
         espacio=espacio-1
         estrellitas=estrellitas+2
         numero=numero+1
     print("\esta es su priamide.")

print(".:programa para hacer piramides:.")
escalon=int(input("introduce el numero de escalones: "))
print(piramide(escalon))
# coding=utf-8

print("Programa para evaluar la expresión alebraica f(x)=3x²+5x-6\n")

x = int(input("Dame el valor de x: "))

funcion = 3 * pow(x,2) + 5 * x - 6

print('El resultado de la funcion es: %s' % funcion)

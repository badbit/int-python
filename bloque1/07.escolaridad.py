# coding=utf-8

print("Programa para determinar la escolaridad de una persona.\n")

edad = int(input("Introduce tu edad: "))

if edad < 3:
	print('No estás en edad escolar.')

elif edad < 6:
	print('Vas en preescolar.')

elif edad < 12:
	print('Vas en primaria.')

elif edad < 16:
	print('Vas en secundaria.')

elif edad < 19:
	print('Vas en preparatoria.')

else:
	print('Espero que sigas estudiando universidad o postgrado.')

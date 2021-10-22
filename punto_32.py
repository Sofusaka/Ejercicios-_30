#Escribe un algoritmo o el respectivo diagrama de flujo que permita determinar si un año dado es o no bisiesto.

print('-----Calcular un año bisiesto------')
año=int(input('Ingrese un año para saber si es bisiesto: '))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
	print(f"El año {año} es bisiesto")
else:
	print(f"El año {año} no es bisiesto")
#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es par o impar.

print('----Pariedad de un número----')
num=int(input('Ingrese un número para saber su pariedad: '))

if num%2==0:        #por medio de la funcion MOD (%) podemos averiguar el residuo de una division, en este caso, si MOD=0, significa que el numero es par
    print(f'El numero {num} es par')
else:
    print(f'El número {num} es impar')
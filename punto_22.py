#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es positivo o negativo

print('----Signos de un número----')
num=int(input('Ingrese un número para saber su signo: '))

if num>=0:        #por medio de una comparacion con 0 podemos saber si el numero es positivo o negativo. 
    print(f'El numero {num} es positivo')
else:
    print(f'El número {num} es negativo')
#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número e indique si este es par-positivo, par-negativo, impar-positivo o impar-negativo.


print('----Signos de un número----')
num=int(input('Ingrese un número para saber su signo: '))

while num>=0:
    if num%2==0:
        print(f'El número {num} es positivo y par')
    else:
        print(f'El número {num} es impar positivo')

while num<0:
    if num%2==0:
        print(f'El número {num} es negativo y par')
    else:
        print(f'El número {num} es impar y negativo')

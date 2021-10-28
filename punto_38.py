#Escribe un algoritmo o el respectivo diagrama de flujo que, dados dos números, verifique si ambos
#están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false

print('=====False and true====')

a=int(input('primer numero: '))
b=int(input('Segundo numero: '))

if 0>a<5 and 0>b<5:
    print('True')

else:
    print('false')
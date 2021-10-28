#Escribe un algoritmo o el respectivo diagrama de flujo que dados 3 números, determine si los números 
# se están incrementando, disminuyendo o ninguno de lo anterior de acuerdo con el orden de digitación.

print('===============Incremento o decremento de numeros==============')

a=int(input('Ingrese el valor del primer numero: '))
b=int(input('Ingrese el valor del segundo numero: '))
c=int(input('Ingrese el valor del tercer numero: '))

if a<b<c:
    print(f'Los números {a}, {b}, {c} están incrementado su valor! ')

if a>b>c:
    print(f'Los números {a}, {b}, {c} están disminuyendo su valor! ')

else:
    print(f'Los números {a}, {b}, {c} no incrementan ni decrementan su valor!')
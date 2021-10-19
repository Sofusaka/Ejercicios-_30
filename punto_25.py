#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este.

print('--------------------------------------')
num=int(input('Ingrese un número: '))
a=num
if num>=10:
    num=num*3
    print(f'el triple de {a} es {num} ')
else:
    num=num/4
    print(f'la cuarta parte de {a} es {num} ')

#Escribe un algoritmo o el respectivo diagrama de flujo que intercambie el valor de dos variables e imprima los valores antes y después del intercambio. 
#Por ejemplo, si a = 1 y b = 3, al intercambiar sus valores serán a = 3 y b = 1 (Consejo: usar variable auxiliar).

print('----Programa que intercambia valores en variables-----------')
a=int(input('Ingrese el valor del primer numero: '))
b=int(input('Ingrese el valor segundo numero: '))

d=b
c=a
a=b
b=c

print(f'el valor del primer numero era {c} y ahora es {a}, el valor del segundo numero era {d} y ahora es {b} ')

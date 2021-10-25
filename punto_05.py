#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número decimal e imprima su parte entera y su parte decimal por aparte.

num=float(input(('Ingrese un numero decimal para hallar su parte entera y su parte decimal: ')))

print(f'La parte entera del numero es {int(num)}')
print(f'la parte decimal del numero es {num-int(num)}')

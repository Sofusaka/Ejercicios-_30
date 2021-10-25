#Escribe un algoritmo o el respectivo diagrama de flujo que calcule el área de un hexágono.

p=int(input('Ingrese el valor del perimetro de un hexagono: '))
ap=int(input('Ingrese el valor de su apotema para hallar el area del hexagono:'))

a=(p*ap)/2

print(f'El valor de el área de un hexagono de perimetro {p} y apotema {ap} es {a}')

#Escribe un algoritmo o el respectivo diagrama de flujo que imprima el área y el perímetro de un círculo.

import math
from typing import AsyncIterable

r=int(input('Ingrese el valor del radio de una circunferencia para hallar su area y perimetro: '))
area=math.pi*(r**2)
perimetro=2*math.pi*r

print(f'El valor de el área de una circunferencia de radio {r} es {area} y su perimetro es {perimetro}')
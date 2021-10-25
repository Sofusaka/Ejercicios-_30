#Escribe un algoritmo o el respectivo diagrama de flujo que determine el tiempo de caída de un objeto que se suelta desde una altura h.

import math
print('-----Calcular el tiempo de caida de un objeto desde altura h---------')
h=float(input('Ingrese la altura desde la que caerá el objeto. Tenga en cuenta dar la distancia en metros (m): '))

t=math.sqrt(2*h/9.806)

print('---------------------------------------------------------------------------------------')
print(f'El tiempo que trascurrirá para que el objeto caiga desde {h} metros es {round(t,3)} segundos')
print('---------------------------------------------------------------------------------------')
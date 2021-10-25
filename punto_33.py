#Escribe un algoritmo o el respectivo diagrama de flujo que permita resolver una ecuación cuadrática
#de tipo ax2 + bx + c (tenga en cuenta las todas las raíces, tanto las reales como las complejas).

from _typeshed import ReadableBuffer
import math

print("-------------------Resolver la ecuación cuadrática ax2 + bx + c-------------------")
a = int(input("Ingrese el valor de a = "))
b = int(input("Ingrese el valor de b = "))
c = int(input("Ingrese la variable independiente c = "))

discriminante=(b**2)-4*a*c

if discriminante<0:
    print('-----La ecuación tiene sus respuestas en los números complejos-----')
    Real=-b/(2*a)
    imaginario=math.sqrt(discriminante)/(2*a)
    print(f'El resultado de x1 en los complejos es {round(2, Real)}+{imaginario}i ')
    print(f'El resultado de x2 en los complejos es {round(2, Real)}-{imaginario}i ')

else:
    print('-----El resultado se encuentra en los numeros reales-----')
    x1=-b+math.sqrt(discriminante)/(2*a)
    x2=-b-math.sqrt(discriminante)/(2*a)
    print(f'El resultado de x1 es igual a {x1} ')
    print(f'El resultado de x2 es igual a {x2} ')

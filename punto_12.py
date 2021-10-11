#Escribe un algoritmo o el respectivo diagrama de flujo que determine la distancia recorrida por un objeto luego de una cantidad de tiempo, 
#si se sabe que va en línea recta y además se conoce su aceleración y su velocidad.

print('-----Calcular la distancia recorrida de un objeto---------')
v=float(input('Ingrese la velocidad inicial del objeto. Tenga en cuenta dar la velocidad en metros (m) por segundos (s): '))
ac=float(input('Ingrese la aceleración del objeto. Tenga en cuenta dar la aceleración en metros (m) por segundos cuadraros (s^2):'))
t=int(input('Ingrese el tiempo recorrido. Recuerde dar el tiempo en segundos (s): '))

d=(v*t)+((ac*t**2)/2)

print('---------------------------------------------------------------------------------------')
print(f'El distancia que recorrerá el objeto en {t} segundos es {round(d,3)} metros')
print('---------------------------------------------------------------------------------------')

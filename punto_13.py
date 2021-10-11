#Escribe un algoritmo o el respectivo diagrama de flujo que determine la velocidad final de un objeto luego de un tiempo, 
#si se sabe que va en línea recta y además se conoce su aceleración.

print('-----Calcular la velocidad final de un objeto---------')
v=float(input('Ingrese la velocidad inicial del objeto. Tenga en cuenta dar la velocidad en metros (m) por segundos (s): '))
ac=float(input('Ingrese la aceleración del objeto. Tenga en cuenta dar la aceleración en metros (m) por segundos cuadraros (s^2):'))
t=int(input('Ingrese el tiempo recorrido. Recuerde dar el tiempo en segundos (s): '))

vf=v+ac*t

print('---------------------------------------------------------------------------------------')
print(f'La velocidad final del objeto es: {round(vf,3)} (m/s)')
print('---------------------------------------------------------------------------------------')
#Escribe un algoritmo o el respectivo diagrama de flujo que dadas coordenadas x1,y1 y x2,y2 en el plano cartesiano calcule la 
# distancia entre ellos (considere todos los valores positivos)
import math

print('-----Calcular distancia entre dos puntos---------')
x1=int(input('Ingrese la coordenada X del primer punto en el plano cartesiano: '))
y1=int(input('Ingrese la coordenada y del segundo punto en el plano cartesiano: '))
x2=int(input('Ingrese la coordenada X del segundo punto en el plano cartesiano: '))
y2=int(input('Ingrese la coordenada y del segundo punto en el plano cartesiano: '))

dis=math.sqrt(((x2-x1)**2)+(y2-y1)**2)

print(f'La distancia entre el punto ({x1},{y1}) y el punto ({x2},{y2}) es {dis}')
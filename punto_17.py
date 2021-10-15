#Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos minutos representan

print('----------Calculadora de segundos a minutos-------------')
seg=int(input('Ingrese la cantidad de segundos que desea compartir en horas: '))

min=seg/60

print(f'>>>>{seg} segundos son equivalentes a {round(min,4)} minutos')
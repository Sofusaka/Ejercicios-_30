#Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántas horas representan


print('----------Calculadora de segundos a horas-------------')
seg=int(input('Ingrese la cantidad de segundos que desea compartir en horas: '))

horas=seg/3600

print(f'>>>>{seg} segundos son equivalentes a {round(horas,4)} horas')
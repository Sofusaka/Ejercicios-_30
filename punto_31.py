#Escribe un algoritmo o el respectivo diagrama de flujo que determine el valor de un pasaje en avión, 
#conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer 
#es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%.
#(el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000).

print('-------Costo de pasaje de avión------')

dis=int(input('Por favor, diga la distancia que recorrerá su vuelo: '))
dias=int(input('Por favor, diga de cuantos dias sera su estancia: '))

precio1=dis*5000
if dis<=20:
    precio1=100000

if dis>1000 and dias>7:
    precio1=precio1*0.15

print('---------------------------------------------')
print(f'Su pasaje tendrá un valor de ${precio1} pesos colombianos')
print('---------------------------------------------')
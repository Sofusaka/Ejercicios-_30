#Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos horas minutos y segundos representan. 
# Por ejemplo si el valor es 86399, imprimirá el siguiente resultado -->  23:59:59

print('----------Calculadora de segundos a horas exactas-------------')
seg=int(input('Ingrese la cantidad de segundos que desea convertir en horas exactas: '))

hora=seg//3600 #hallamos la cantidad de horas que hay en n segundos. Usamos division entera para dar un resultado más estético

seg=seg%3600   #Usamos la función MOD(%) para saber lo que nos queda, es decir, el residuo a calcular

min= seg//60   #Hallamos la cantidad de minutos que hay en los segundos restantes.

seg= seg%60    #Los segundos serán el residuo entre la cantidad de segundos y 60 (60 es la cantidad de seg en un minuto)

print('--------------------------------------------------------------------')
print(f'>>>> {seg} segundos son equivalentes a {hora}:{min}:{seg}, es decir, {hora} horas, {min} minutos, y {seg} segundos. ')
print('--------------------------------------------------------------------')


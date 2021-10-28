#Escribe un algoritmo o el respectivo diagrama de flujo que lea un número del día de la 
# semana (entre 1 y 7) e indique el nombre del día. Por ejemplo:  1 ---> Lunes ; 5 ---> Viernes

numeros={'1':'Lunes','2':'Martes','3':'Miércoles','4':'Jueves','5':'Viernes'
,'6':'Sábado','7':'Domingo'}

print('=====Días de la semana=====')

num=input('Ingrese un número que corresponda al día de la semana: ')

print(f'El número {num} corresponde al día de la semana {numeros.get(num)}')
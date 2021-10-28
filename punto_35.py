#Escribe un algoritmo o el respectivo diagrama de flujo que dado un número entre 0 y 10, imprima el nombre del número. 

numeros={'0':'cero', '1':'uno','2':'dos','3':'tres','4':'cuatro','5':'cinco'
,'6':'seis','7':'siete','8':'ocho','9':'nueve','10':'diez'}

num=input('Ingrese un número entre 0 y 10: ')

print(f'El nombre del numero es {numeros.get(num)}')
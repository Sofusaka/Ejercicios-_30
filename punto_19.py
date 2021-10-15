#Escribe un algoritmo o el respectivo diagrama de flujo que, dada una cantidad de dinero, 
# determine la menor cantidad de billetes de cada denominación que se puede entregar.

print('----------Calculadora de billetes----------')

dinero=int(input('Ingrese la cantidad de dinero que desea convertir a cantidad de billetes: '))

# Realizaremos un menú para que la persona pueda escoger el tipo de billete que prefiera:
#para eso, le asignaremos numeros a cada tipo de billete:
#
#1--> billete de mil
#2--> billete de 2k
#3--> billete de 5k
#4--> billete de 10k
#5--> billete de 20k
#6--> billete de 50k
#7--> billete de 100k

#Ahora, definimos funciones para cada uno de los billetes, realizando una division entera entera  entre la cantidad de dinero y el valor del billete. 

def mil (a): #1--> billete de mil
    cantidad= dinero//1000
    return cantidad

def dosmil (dinero): #2--> billete de 2k
    cantidad= dinero//2000
    return cantidad
    
def cincomil (dinero): #3--> billete de 5k
    cantidad= dinero//5000
    return cantidad

def diezmil (dinero): #4--> billete de 10k
    cantidad= dinero//10000
    return cantidad

def veintemil (dinero): #5--> billete de 20k
    cantidad= dinero//20000
    return cantidad

def cincuentamil (dinero): #6--> billete de 50k
    cantidad= dinero//50000
    return cantidad

def cienmil (dinero): #7--> billete de 100k
    cantidad= dinero//100000
    return cantidad
 #Creamos el menú para que el usuario escoja el tipo de billete
menu=input('Seleccione el tipo de billete:\n 1--> billete de mil\n 2--> billete de 2k\n 3--> billete de 5k\n 4--> billete de 10k\n 5--> billete de 20k\n 6--> billete de 50k\n 7--> billete de 100k\n 8-->Imprimir todas las posibilidades\n')

if menu=='1': 
    
    print(f'La cantidad de billetes que se pueden imprimir es {mil(dinero)}')

if menu=='2':
  
    print(f'La cantidad de billetes que se pueden imprimir es {dosmil(dinero)}')

if menu=='3':
    
    print(f'La cantidad de billetes que se pueden imprimir es {cincomil(dinero)}')

if menu=='4':
    
    print(f'La cantidad de billetes que se pueden imprimir es {diezmil(dinero)}')

if menu=='5':
   
    print(f'La cantidad de billetes que se pueden imprimir es {veintemil(dinero)}')

if menu=='6':
    
    print(f'La cantidad de billetes que se pueden imprimir es {cincuentamil(dinero)}')

if menu=='7':
   
    print(f'La cantidad de billetes que se pueden imprimir es {cienmil(dinero)}')

if menu=='8':
   
    print(f'La cantidad de billetes que se pueden imprimir en billetes de mil es {mil(dinero)}, en billetes de dos mil {dosmil(dinero)}, en billetes de cinco mil {cincomil(dinero)}, en billetes de diez mil {diezmil(dinero)}, en billetes de veinte mil {veintemil(dinero)}, en billetes de cincuenta mil {cincuentamil(dinero)}, y en billetes de cien mil {cienmil(dinero)} ')
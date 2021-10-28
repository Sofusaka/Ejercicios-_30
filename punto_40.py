#Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al menos 2 de ellos son iguales

print('=====Comparación entre 3 números=====')
num=[]

n=int(input('Ingrese la cantidad de números que quiere ingresar: '))

for i in range (n):
    numero=int(input('Ingrese el valor del número: '))
    num.append(numero)

if len(num)==len(set(num)):
    print('No hay números repetidos!')  #La funcion set() convierte a una lista en un conjunto sin valores repetidos
                                        #entonces si ambos largos son iguales significa que no hay numeros repetidos

else:
    print('Hay números repetidos!')
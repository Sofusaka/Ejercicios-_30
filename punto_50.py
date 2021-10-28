#Escribe un algoritmo o el respectivo diagrama de flujo para leer una cantidad variable de números 
# e indicar el promedio de los números pares y el promedio de los números impares.

numerospares=[]
numerosimpares=[]
n=int(input('Ingrese la cantidad de numeros con los que va a operar: '))
for i in range (n):
        num=int(input('Ingrese un numero: '))
        if num%2==0:
            numerospares.append(num)
        else:
            numerosimpares.append(num)

print(f'El promedio de los numeros impares {numerosimpares} es {sum(numerosimpares)/len(numerosimpares)} y el promedio de los pares {numerospares} es {sum(numerospares)/len(numerospares)}')
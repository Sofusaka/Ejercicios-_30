#Escribe un algoritmo o el respectivo diagrama de flujo que lea n números y calcule su suma y su promedio

numeros=[]
n=int(input('Ingrese la cantidad de numeros con los que va a operar: '))
for i in range (n):
        num=int(input('Ingrese un numero: '))
        numeros.append(num)

print(f'La sumatoria de los números es {sum(numeros)} y su promedio es {sum(numeros)/len(numeros)}')
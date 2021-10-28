#Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 números y calcule su suma y su promedio

numeros=[]

for i in range (10):
        num=int(input('Ingrese un numero: '))
        numeros.append(num)

print(f'La sumatoria de los números es {sum(numeros)} y su promedio es {sum(numeros)/len(numeros)}')
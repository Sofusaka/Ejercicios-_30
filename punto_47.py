#Escribe un algoritmo o el respectivo diagrama de flujo que determine la suma de los números naturales contenidos entre dos números n y m (verificar que m>n)

print('====Suma de números naturales=====')

numeros=[]
n=int(input('Ingrese el número desde donde quiere iniciar el conteo: '))
m=int(input('Ingrese el número desde donde quiere finalizar el conteo: '))

if n<m:
    for i in range (n+1,m):
        
            numeros.append(i)
    print(f'La sumatoria de los números entre {n} y {m} es {sum(numeros)}')

else:
    print('Los números ingresados no son válidos')
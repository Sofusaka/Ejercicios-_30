#Escribe un algoritmo o el respectivo diagrama de flujo que imprima los números naturales contenidos entre dos números n y m

print('====Números naturales=====')

n=int(input('Ingrese el número desde donde quiere iniciar el conteo: '))
m=int(input('Ingrese el número desde donde quiere finalizar el conteo: '))

if n<m:
    for i in range (n,m):
    
        print(i)

else:
    print('Los números ingresados no son válidos')


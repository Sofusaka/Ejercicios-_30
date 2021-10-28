#Escribe un algoritmo o el respectivo diagrama de flujo que dado un número n, imprima los números entre 1 y n siguiendo la siguiente secuencia: 1   -2   3  -4   5  -6 

n=int(input('Ingrese la cantidad de números que quiere calcular: '))
for i in range (1,n):

    if i%2==0:
        print(i-(2*i))
    else:
        print(i)

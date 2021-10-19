#Escribe un algoritmo o el respectivo diagrama de flujo que, dada un numero de 4 cifras, 
# reordene sus dígitos de manera inversa. Por ejemplo 3245 ---> 5423

print('----Reordenar numeros de 4 digitos----')

def invertido(a):
    invert=int(str(a)[::-1]) #Lo de [::-1] es un "truco" frecuentemente usado en python para obtener una lista o una cadena "del revés". 
    return invert

num=input('Ingrese un número de 4 cifras para invertirlo: ')
while len(num)!=4: #como el problema nos define un límite de 4 digitos, marcamos los parámetros por medio de una funcion ciclica 
        print('----------------------------------------------------------------')
        print('El número es incorrecto. Recuerde que tiene que ser un número de 4 cifras.')
        num=input('Ingrese un número de 4 cifras para invertirlo: ')                #usamos un loop hasta que el usuario ingrese el numero correctamente
        print('----------------------------------------------------------------')
else:
    print('----------------------------------------------------------------')
    print(f'El número {num} invertido es {invertido(num)}')
    print('----------------------------------------------------------------')





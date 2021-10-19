#Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero.

num1=[]
print('--------------------------Calcular en número máximo y mínimo-------------------------------')

for i in range (2):
    valor=int(input('ingrese el valor del número: '))
    num1.append(valor)

valor=int(input('ingrese el valor del número: '))

if sum(num1)> valor:

        print('------------------------------------------------------------------------')
        print(f'la suma de los dos primeros digitos {num1}= {sum(num1)} es mayor que el tercer digito: {valor}')
        print('------------------------------------------------------------------------')

else:
    print('------------------------------------------------------------------------')
    print(f'la suma de los dos primeros digitos {num1}= {sum(num1)} es menor que el tercer digito: {valor}')
    print('------------------------------------------------------------------------')
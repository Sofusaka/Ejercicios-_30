#Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero.

num=[]
print('--------------------------Calcular en número máximo y mínimo-------------------------------')
cnum=int(input('Ingrese la cantidad de números que va a comparar: '))

for i in range (3):
    valor=int(input('ingrese el valor del número: '))
    num.append(valor)

if sum(num[0,1])>num[2]:

        print('------------------------------------------------------------------------')
        print(f'la suma de los dos primeros digitos es mayor que el tercer digito')
        print('------------------------------------------------------------------------')
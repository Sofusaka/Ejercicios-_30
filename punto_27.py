#Escribe un algoritmo o el respectivo diagrama de flujo que lea dos números y determine el mayor de ellos.

num=[]
print('--------------------------Calcular en número máximo-------------------------------')
cnum=int(input('Ingrese la cantidad de números que va a comparar: '))

for i in range (cnum):
    valor=int(input('ingrese el valor del número: '))
    num.append(valor)
print('------------------------------------------------------------------------')
print(f'El número mayor de los números ingresados {num} es: {max(num)}')
print('------------------------------------------------------------------------')
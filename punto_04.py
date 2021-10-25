#Escribe un algoritmo o el respectivo diagrama de flujo para imprimir la suma, resta, multiplicación, división y residuo de dos números dados.

def suma(no1,no2): #Funcion que define la suma de los dos numeros
    sum=no1+no2
    return sum

def resta(no1,no2): #Funcion que define la resta de los dos numeros
    res=no1-no2
    return res

def multiplicacion(no1,no2): #Funcion que define la multiplicacion de los dos numeros
    mult=no1*no2
    return mult

def division(no1,no2): #Funcion que define la division de los dos numeros
    div=no1/no2
    return div

def residuo(no1,no2): #Funcion que define el residuo de los dos numeros
    resi=no1%no2
    return resi

#Ingreso de los dos numeros por teclado#

print('---Calculadora de operaciones basicas---') #Ingreso de los dos numeros por teclado
num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))

#Ejecucion e impresion de las funciones con los numeros ingresados por teclado#

print(f'La suma de {num1} y {num2} es: ', suma(num1,num2))
print(f'La resta de {num1} y {num2} es: ', resta(num1,num2))
print(f'La multiplicacion de {num1} y {num2} es: ', multiplicacion(num1,num2))
print(f'La division de {num1} y {num2} es: ', division(num1,num2))
print(f'El residuo de {num1} y {num2} es: ', residuo(num1,num2))


#Escribe un algoritmo o el respectivo diagrama de flujo que dados tres números calcule el promedio de dichos números.

print('---calcular el promedio---')

pn=int(input('ingrese cuantos numeros quiere hallar su promedio: '))
a=0
for i in range (pn): 
    p1=int(input('ingrese el valor del numero: '))
    a=a+p1

promedio=(a)/i+1
print(f'el valor del promedio es {promedio} ')


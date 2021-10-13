#Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) 
# de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s).

c=299792458
print('-----Calcular la energia de un objeto---------')
m=int(input('Ingrese el peso de un objeto para calcular la cantidad de energia. Recuerde ingresarla en Kg: '))

e=m*c**2

print('---------------------------------------------------------------------------------------')
print(f'La energia del objeto es: {round(c,3)} Jules')
print('---------------------------------------------------------------------------------------')
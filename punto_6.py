#Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta realizada, 
# indicando el valor original, el valor del IVA y el valor de la venta con IVA incluido.

print('----- Calculadora de IVA al 19% -----')
precio1=int(input('Ingrese el precio de un producto: ')) #Se ingresa el valor de un producto sin IVA

iva=precio1*0.19 #Se calcula el valor del IVA
iva2=precio1+iva #
print('-----------------------------------------')
print(f'El costo sin IVA es ${precio1}, el IVA es ${iva}, y el total con iva es ${iva2}')
print('-----------------------------------------')

#Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta, si esta es mayor o igual 150.000 aplicar un descuento del 5%

def ivasin (precio):
    iva=precio*0.19 
    total=precio+iva
    return iva, total

def ivacon (precio):
    desc=precio*0.05
    precio=precio-desc
    iva=precio*0.19
    total=precio+iva
    return desc, iva, total

print('----- Calculadora de descuentos e IVA al 19% -----')
precio1=int(input('Ingrese el precio de un producto: ')) #Se ingresa el valor de un producto sin IVA


if precio1>=190000:
    print('-----------------------------------------')
    print(f'El costo sin IVA es ${precio1},\nel descuento es ${ivacon(precio1)[0]}\nel IVA es ${ivacon(precio1)[1]}\ny el total a pagar es ${ivacon(precio1)[2]}')#con la funcion ivacon se realiza la funcion iva con descuento, y la sintaxis ivacon(precio1)[1] significa funcion(variable)[orden de la variable a llamar en la tupla]
    print('-----------------------------------------')

else:
    print('-----------------------------------------')
    print(f'El costo sin IVA es ${precio1},\nel IVA es ${ivasin(precio1)[0]}\nel total a pagar es ${ivacon(precio1)[1]}')#con la funcion ivasin se realiza la funcion iva sin, y la sintaxis ivacon(precio1)[1] significa funcion(variable)[orden de la variable a llamar en la tupla]
    print('-----------------------------------------')

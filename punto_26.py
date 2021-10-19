#Escribe un algoritmo o el respectivo diagrama de flujo que lea las cinco notas obtenidas por un estudiante y calcule su nota final, 
# sabiendo que las cada nota tiene el siguiente valor: n1 (15%), n2 (20%), n3 (15%), n4 (30%), n5 (20%). Si la nota obtenida
# es menor a 2,0 deberá indicarle al estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es mayor o 
# igual a 3 deberá indicar que aprobó y si es mayor a 4,5 
# extenderá un mensaje de felicitación al estudiante.

print('------Notas final de estudiantes-----')

nestud=int(input('Ingrese la cantidad de estudiantes a los que le quiere calcular su nota final: '))

for i in range (nestud):
    n1=int(input(f'Ingrese la primera nota del estudiante {i+1}: '))
    n2=int(input(f'Ingrese la segunda nota del estudiante {i+1}: '))
    n3=int(input(f'Ingrese la tercera nota del estudiante {i+1}: '))
    n4=int(input(f'Ingrese la cuarta nota del estudiante {i+1}: '))
    n5=int(input(f'Ingrese la quinta nota del estudiante {i+1}: '))

    promedio=n1*0.15+n2*0.2+n3*0.15+n4*0.3+n5*0.2

    if promedio>=4.5:
        print('-----------------------------------------------------------------------------------------------')
        print(f'Felicidades estudiante {i+1}! Has aprobado con una nota sobresaliente, la cual corresponde a {promedio}')
        print('-----------------------------------------------------------------------------------------------')

    if promedio>=3:
        print('---------------------------------------')
        print(f'El estudiante {i+1} aprobó el curso')
        print('---------------------------------------')
    else:
        print('---------------------------------------')
        print(f'El estudiante {i+1} reprobó el curso')
        print('---------------------------------------')
        if promedio<2:
            print('---------------------------------------')
            print(f'El estudiante {i+1} no puede habilitar')
            print('---------------------------------------')


print('Fin del programa')

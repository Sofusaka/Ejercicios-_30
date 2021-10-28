#Escribe un algoritmo o el respectivo diagrama de flujo que, dado un usuario y una contraseña predefinida (por ejemplo usuario=”carlos" y contraseña=”1234”, 
# le permita a un usuario digital su usuario y contraseña y enviar un mensaje de inicio de sesión si lo digitado corresponde al usuario y contraseña predefinida.

print('-------Registrarse-------')
iniciar={'Usuario':'','Contraseña':''}
iniciar['Usuario']= input('Ingrese un nombre de usuario: ')
iniciar['Contraseña']= input('Ingrese una contraseña: ')

print('\n------Inicio de sesión------\n')
user=input('Ingrese su usuario: ')
clave=input('Ingrese su contraseña: ')

if user==iniciar.get('Usuario') and clave==iniciar.get('Contraseña'):
    print(iniciar['Usuario'],',Usted ha iniciado sesión exitosamente!')

else:
    print('Usted no ha iniciado sesión. Revise su usuario o contraseña')



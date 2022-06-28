def imprimir_mensaje():   # * asi se escriben las funciones
  print('Mensaje especial: ')
  print('Estoy aprendiendo a usar funciones')

imprimir_mensaje()



def conversacion(mensaje):    # * Asi se pasan los parametros en python
  print('Hola')
  print('Como estas?')
  print(mensaje)
  print('Adios')

opcion = int(input('Elige una opcion (1, 2, 3,): '))
if opcion == 1:
  conversacion('Elegiste la opcion 1')
if opcion == 2:
  conversacion('Elegiste la opcion 2')
if opcion == 3:
  conversacion('Elegiste la opcion 3')
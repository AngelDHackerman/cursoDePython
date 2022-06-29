def conversor (tipo_pesos, valor_dolar):
  pesos = input('Cuantos pesos ' + tipo_pesos + ' tienes?: ')
  pesos = float(pesos)
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + 'dolares')

# De quetzales a dolares

# quetzales = input('Cuantos quetzales tienes?: ')
quetzales = 100
quetzales = float(quetzales) # float convierte un string a un numero decimal
valor_dolar = 7.78
dolares = quetzales / valor_dolar
dolares = round(dolares, 2) # el segundo parametro indica cuantos decimales queremos
dolares = str(dolares)
print('Tienes $' + dolares + ' Dolares')


        # Pesos colombianos, argentinos y mexicanos

menu = '''
Bienvenido al conversor de monedas 

1 - Pesos colombianos 
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: '''

opcion = int(input(menu))

if opcion == 1:
  conversor('colombianos', 4060)
elif opcion == 2:
  conversor('argentinos', 120)
elif opcion == 3:
  conversor('mexicanos', 24)
else:
  print('Ingresa una opcion correcta por favor.')



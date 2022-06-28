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
  pesos = input('Cuantos pesos colombianos tienes?: ')
  pesos = float(pesos)
  valor_dolar = 4132
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + 'dolares')
elif opcion == 2:
  pesos = input('Cuantos pesos argentinos tienes?: ')
  pesos = float(pesos)
  valor_dolar = 160
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + 'dolares')
elif opcion == 3:
  pesos = input('Cuantos pesos colombianos tienes?: ')
  pesos = float(pesos)
  valor_dolar = 20
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + 'dolares')
else:
  print('Ingresa una opcion correcta por favor.')



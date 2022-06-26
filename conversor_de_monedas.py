# De quetzales a dolares

quetzales = input('Cuantos quetzales tienes?: ')
quetzales = float(quetzales) # float convierte un string a un numero decimal
valor_dolar = 7.78
dolares = quetzales / valor_dolar
dolares = round(dolares, 2) # el segundo parametro indica cuantos decimales queremos
dolares = str(dolares)
print('Tienes $' + dolares + ' Dolares')

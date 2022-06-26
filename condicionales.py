edad = int(input('Escribe tu edad: '))

if edad > 17:
  #pass    # ? pass, significa que aqui escribiremos codigo pero lo dejamos para despues
  print('Eres mayor de edad')
else:
  print('Eres menor de edad')



numero = int(input('Escribe un numero: '))

if numero > 5:
  print('Es mayor a 5')
elif numero == 5:   # ? elif es el equivalente a else if en javascript
  print('Es igual a 5')
else: 
  print('Es menor a 5')
def run():
  mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
  }
  print(mi_diccionario['llave2'])

  poblacion_paises = {
    'Argentina': 44_938_712,
    'Brasil': 210_147_125,
    'Colombia': 50_372_424,
  }
  print(poblacion_paises['Argentina'])
  
  print('\n Imprimiendo las llaves .keys(): ')
  for pais in poblacion_paises.keys(): # ? .keys() nos devuelve las llaves del objeto.
    print(pais)

  print('\n Imprimiendo los valores .values(): ')
  for poblacion in poblacion_paises.values(): # ? .values() nos devuelven los valores de el diccionario
    print(poblacion)

  print('\n Imprimiendo llaves y valores con .items():')
  for pais, poblacion in poblacion_paises.items():
    print(pais, 'tiene', poblacion, 'habitantes')
  

if __name__ == '__main__':
  run()
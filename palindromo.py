def palindromo(palabra):
  palabra = palabra.replace(' ', '') # Esto elimina los espacios de las oraciones
  palabra = palabra.lower() # Hace todas las letras minusculas
  palabra_invertida = palabra[::-1] # ? palabra[::-1] asi es como se invierten las palabras en python
  if palabra == palabra_invertida:
    return True
  else:
    return False
                            # Siempre se deben dejar 2 espacios entre funciones en python

def run():
  palabra: input('Escribe una plabra: ')
  es_palindromo = palindromo(palabra)
  if es_palindromo == True:
    print('Es un palindromo')
  else:
    print('No es palindromo')


if __name__ == '__main__': # todo: Esto es el entry point de python, toda vez python se encuentra con esto, empieza a correr todo lo que esta debajo.
  run()

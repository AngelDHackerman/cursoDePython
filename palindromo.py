def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    
    if palabra[::] == palabra[::-1]: # ? palabra[::-1], asi se invierten las palabras en python
        return True
    
    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ')
    if es_palindromo(palabra):
        print('Es palindromo')

    else:
        print('No es palindromo')


if __name__ == "__main__": #todo: esta linea es el entry point. Por aqui python va a comenzar a correr el codigo
    run()
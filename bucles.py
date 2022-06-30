def run():
  LIMITE = 1_000_000  # ? con todas las letras en MAYUSCULAS se definen las variables en python.

  contador = 0
  potencia_2 = 2 ** contador
  while potencia_2 <= LIMITE: # * while, bucle identico al de JS
    print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
    contador = contador + 1
    potencia_2 = 2 ** contador


if __name__ == '__main__':
  run()
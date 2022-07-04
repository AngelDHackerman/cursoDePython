def run():
  for contador in range(50 + 1):
    if contador % 2 != 0:
      continue    # ? Si el residuo no es 0, se va a saltar la vuelta ejecutada ( o continuar a la siguiente )
    print(contador)   # 2, 4, 6, 8, 10...


    for i in range(5000):
      print(i)
      if i == 1995:
        break   # ? Si la condicion se cumple el ciclo debe "frenar" o bien se debe "cortar". 


if __name__ == '__main__':    # * recuerda que este es el entry point
  run()
import random


def generate_password():
  MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
  MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
  CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
  NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

  caracteres = MAYUS + MINUS + CHARS + NUMS

  password = []

  for i in range(30):
    caracter_random = random.choice(caracteres) # ? .choice() me permite elegir un caracter random de el array de caracteres. 
    password.append(caracter_random)

  password = "".join(password)  # todo: "".join(array) asi es como se une un array de varios valores en un solo string
  return password


def run():
  password = generate_password()
  print('Tu nueva contraseña es: ', password)


if __name__ == '__main__':
  run()
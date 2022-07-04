
      # ? Ciclo for

for y in range(10):
  print(y)


limite = 30
for x in range(limite + 1):  # range(), es la forma de iterar en secuencias numericas, sino agregamos el +1, el bucle se detiene un numero abajo 
  print(x)


a = list(range(30))   # ! Asi se convierte un rango en un array.
print(a)

for x in range(5, 20 + 1):    # ? range(5, 20 + 1) 5 es el valor INICIAL  y 20 es el valor FINAL
  print(x)
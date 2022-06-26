          # ? Variables

numero = 10
numero2 = 16

numero3 = numero + numero2

print(numero3)


nombre = 'Angel '   # hay un " " al final
apellido = 'Hackerman'

print(nombre + apellido)

print(nombre * 4) # * Asi se puede multiplicar este string

es_estudiante = True
print("Es estudiante: ",es_estudiante)



          # ? Convertir un dato a un tipo diferente

    # De string a numero 

entrada1 = int(input('Escribe un numero: '))   # Este es el equivalente al prompt de javascript
entrada2 = int(input('Escribe otro numero: '))  # todo: int() es el equivalente a parseInt()
entrada = entrada1 + entrada2

print(entrada)

    # De decimal a entero

numero_decimal = 4.5
print(int(numero_decimal))

    # De numero a string

print(str(numero_decimal))   # todo: str() convierte los valores a string
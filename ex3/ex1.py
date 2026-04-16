# ex1 (✿◠ᴗ◠)

pares = 0
impares = 0
contador = 0
numero = 1

while contador < 30:
    if numero % 2 == 0:
        print("par:", numero)
        pares = pares + 1
    else:
        print("impar:", numero)
        impares = impares + 1

    numero = numero + 1
    contador = contador + 1
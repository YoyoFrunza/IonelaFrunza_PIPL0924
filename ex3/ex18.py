# ex18 (✿◠ᴗ◠)

limite = int(input("limite: "))

numero = 1
quantidade_perfeitos = 0

while numero <= limite:

    soma_divisores = 0
    divisor = 1

    # soma todos os divisores do numero
    while divisor < numero:
        if numero % divisor == 0:
            soma_divisores = soma_divisores + divisor
        divisor = divisor + 1

    # se for numero perfeito
    if soma_divisores == numero:
        quantidade_perfeitos = quantidade_perfeitos + 1

    numero = numero + 1

print("numeros perfeitos:", quantidade_perfeitos)
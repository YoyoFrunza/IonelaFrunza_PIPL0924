# ex16 (✿◠ᴗ◠)

soma_numeros = 0
quantidade_numeros = 0

while quantidade_numeros < 30:

    numero = int(input("numero entre 1 e 50: "))

    # verifica se esta entre 1 e 50 e se e par
    if numero >= 1 and numero <= 50 and numero % 2 == 0:
        soma_numeros = soma_numeros + numero  # soma o numero valido
        quantidade_numeros = quantidade_numeros + 1  # conta numero valido
    else:
        print("numero invalido")

media = soma_numeros / 30 
print("media:", media)
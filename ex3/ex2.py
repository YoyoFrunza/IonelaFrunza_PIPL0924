# ex2 (✿◠ᴗ◠)

pares = 0
impares = 0

for x in range(10):
    numero = int(input("numero: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("pares:", pares)
print("impares:", impares)
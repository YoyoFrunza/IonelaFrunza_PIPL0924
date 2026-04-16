# ex10 (✿◠ᴗ◠)

numero = int(input("numero: "))

divisores = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        divisores = divisores + 1

print("divisores:", divisores)
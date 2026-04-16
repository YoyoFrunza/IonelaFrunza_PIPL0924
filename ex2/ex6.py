# ex6 (✿◠ᴗ◠)

cliente = input("cliente: ")
compra = float(input("compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

total = compra - desconto

print("nome:", cliente)
print("compra:", compra)
print("desconto:", desconto)
print("total a pagar:", total)
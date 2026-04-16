# ex4 (✿◠ᴗ◠)

saldo = float(input("saldo: "))
cheque = float(input("cheque: "))

if cheque <= saldo:
    saldo = saldo - cheque
    print("cheque descontado, saldo:", saldo)
else:
    print("cheque nao pode ser descontado")
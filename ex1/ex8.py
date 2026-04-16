# ex8 (✿◠ᴗ◠)

operacao = input("operacao(soma/sub/mult/div): ")
numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))

match operacao:
    case "soma":
        print(numero1 + numero2)

    case "sub":
        print(numero1 - numero2)

    case "mult":
        print(numero1 * numero2)

    case "div":
        print(numero1 / numero2)

    case _:
        print("operacao invalida")
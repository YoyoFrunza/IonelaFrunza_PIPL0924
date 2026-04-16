# ex4 (✿◠ᴗ◠)
valor = input("valor: ")

match valor:
    case valor if valor.isdigit():
        print("numero inteiro")

    case valor if "." in valor and valor.replace(".", "").isdigit():
        print("numero decimal")

    case valor if valor.startswith("[") and valor.endswith("]"):
        print("lista")

    case valor if valor.isalpha():
        print("string textual")

    case _:
        print("tipo desconhecido")
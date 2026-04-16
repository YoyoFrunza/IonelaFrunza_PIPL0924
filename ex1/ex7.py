# ex7 (✿◠ᴗ◠)

categoria = input("categoria(eletronico/alimentar): ")
preco = int(input("preco: "))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case {"categoria": "eletronico", "preco": preco} if preco > 1000:
        print("produto de luxo")

    case {"categoria": "eletronico"}:
        print("produto comum")

    case {"categoria": "alimentar"}:
        print("produto alimento")

    case _:
        print("categoria desconhecida")
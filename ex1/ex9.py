# ex9 (✿◠ᴗ◠)

metodo = input("metodo: ").upper()
conteudo = input("conteudo: ")

requisicao = {"metodo": metodo, "conteudo": conteudo}

match requisicao:
    case {"metodo": "GET"}:
        print("requisicao get recebida")

    case {"metodo": "POST", "conteudo": ""}:
        print("requisicao post sem dados")

    case {"metodo": "POST", "conteudo": conteudo}:
        print("requisicao post com dados validos")

    case _:
        print("metodo nao suportado")
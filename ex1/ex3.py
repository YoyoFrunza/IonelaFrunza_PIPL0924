# ex3 (✿◠ᴗ◠)

tipo = input("tipo(compra/venda): ")
valor = int(input("valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido["tipo"]:
    case "compra":
        print("compra de", pedido["valor"], "€")
    case "venda":
        print("venda de", pedido["valor"], "€")
    case _:
        print("pedido desconhecido")
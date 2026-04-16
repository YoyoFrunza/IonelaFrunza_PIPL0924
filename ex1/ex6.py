# ex6 (✿◠ᴗ◠)

status = input("status: ")
tempo_resposta = int(input("tempo de resposta: "))

servidor = {"status": status, "tempo_resposta": tempo_resposta}

match servidor:
    case {"status": "erro"}:  #meter 0 no tempo resposta para funcionar
        print("servidor indisponivel")

    case {"status": "ok", "tempo_resposta": tempo_resposta} if tempo_resposta > 200:
        print("servidor lento")

    case {"status": "ok"}:
        print("servidor ativo")

    case _:
        print("estado desconhecido")
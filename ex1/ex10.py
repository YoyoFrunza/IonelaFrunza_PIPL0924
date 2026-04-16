# ex10 (✿◠ᴗ◠)

jogador1 = input("jogador 1: ")
jogador2 = input("jogador 2: ")

match (jogador1, jogador2):
    case (jogador1, jogador2) if jogador1 == jogador2:
        print("empate")

    case ("pedra", "tesoura"):
        print("jogador 1 venceu")

    case ("tesoura", "papel"):
        print("jogador 1 venceu")

    case ("papel", "pedra"):
        print("jogador 1 venceu")

    case _:
        print("jogador 2 venceu")
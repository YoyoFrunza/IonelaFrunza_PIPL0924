# ex1 (✿◠ᴗ◠)

dia = input("dia: ")

match dia:
    case "sábado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia invalido")
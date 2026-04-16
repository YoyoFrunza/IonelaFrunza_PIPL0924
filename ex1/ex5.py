# ex5 (✿◠ᴗ◠)

mensagem = input("mensagem: ")

match mensagem:
    case "ola" | "bom dia":
        print("saudacao")

    case mensagem if mensagem.endswith("?"):
        print("pergunta")

    case mensagem if "tchau" in mensagem or "adeus" in mensagem:
        print("despedida")

    case _:
        print("mensagem generica")
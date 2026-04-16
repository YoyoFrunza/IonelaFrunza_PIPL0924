# ex2 (✿◠ᴗ◠)

nota = int(input("nota: "))

match nota:
    case n if n >= 90:
        print("excelente")
    case n if n >= 70:
        print("bom")
    case n if n >= 50:
        print("suficiente")
    case _:
        print("insuficiente")
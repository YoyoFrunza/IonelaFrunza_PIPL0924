# teste final parte 1 (✿◠ᴗ◠)

while True:

    print("\n--- MENU ---")
    print("1 - analisar numeros")
    print("2 - calculadora")
    print("3 - tabuada")
    print("0 - sair")

    opcao = int(input("escolhe opcao: "))

    # ---------------- ANALISE ----------------
    if opcao == 1:

        numero_inicial = int(input("numero (1 a 30000): "))

        if numero_inicial < 1 or numero_inicial > 30000:
            print("numero invalido")
        else:

            passo = 0

            while passo <= 10:

                numero = numero_inicial - passo

                if numero < 1:
                    break

                # conta divisores
                divisores = 0
                contador = 1

                while contador <= numero:
                    if numero % contador == 0:
                        divisores = divisores + 1
                    contador = contador + 1

                # primo
                if divisores == 2:
                    print(numero, "e primo")

                print(numero, "tem", divisores, "divisores")

                # perfeito
                soma = 0
                contador = 1

                while contador < numero:
                    if numero % contador == 0:
                        soma = soma + contador
                    contador = contador + 1

                if soma == numero:
                    print(numero, "e perfeito")

                passo = passo + 1

            continuar = input("continuar? (s/n): ")
            if continuar == "n":
                break

    # ---------------- CALCULADORA ----------------
    elif opcao == 2:

        n1 = float(input("numero 1: "))
        n2 = float(input("numero 2: "))
        op = input("operacao (+,-,*,/): ")

        if op == "+":
            print(n1 + n2)
        elif op == "-":
            print(n1 - n2)
        elif op == "*":
            print(n1 * n2)
        elif op == "/":
            print(n1 / n2)
        else:
            print("invalido")

    # ---------------- TABUADA ----------------
    elif opcao == 3:

        maximo = int(input("numero (1 a 1000): "))

        if maximo < 1 or maximo > 1000:
            print("invalido")
        else:

            numero = 1

            while numero <= maximo:

                print("\ntabuada do", numero)

                multiplicador = 1

                while multiplicador <= 10:
                    print(numero, "x", multiplicador, "=", numero * multiplicador)
                    multiplicador = multiplicador + 1

                numero = numero + 20  # de 20 em 20

    # ---------------- SAIR ----------------
    elif opcao == 0:
        break

    else:
        print("opcao invalida")
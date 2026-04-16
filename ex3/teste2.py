# teste final parte 2 (✿◠ᴗ◠)

import os  

def limpar():
    os.system("cls")


clientes = [] 

while True:

    #menu principal
    print("\n--- CLIENTES ---")
    print("1 - adicionar cliente")
    print("2 - listar clientes")
    print("3 - procurar cliente")
    print("0 - sair")

    opcao = int(input("escolhe: "))

    # ---------------- ADICIONAR CLIENTE ----------------
    if opcao == 1:

        limpar() 

        #pede dados do cliente
        nome = input("nome: ")
        morada = input("morada: ")
        telefone = input("telefone: ")
        nif = input("nif: ")
        compra = float(input("compra: "))

        #calcula o desconto
        if compra <= 200:
            desconto = compra * 0.05
        elif compra <= 500:
            desconto = compra * 0.10
        else:
            desconto = compra * 0.15

        #calcula o valor final
        valorfinal = compra - desconto

        #cria uma lista com todos os dados
        cliente = [len(clientes)+1, nome, morada, telefone, nif, compra, valorfinal]

        #adiciona cliente à lista principal
        clientes.append(cliente)

        print("\ncliente adicionado!")

    # ---------------- LISTAR CLIENTES ----------------
    elif opcao == 2:

        limpar()

        print("--- LISTA DE CLIENTES ---\n")

        contador = 0  #começa no primeiro cliente

        #percorre todos os clientes
        while contador < len(clientes):

            #mostra os dados do cliente atual
            print("numero:", clientes[contador][0])
            print("nome:", clientes[contador][1])
            print("morada:", clientes[contador][2])
            print("telefone:", clientes[contador][3])
            print("nif:", clientes[contador][4])
            print("compra:", clientes[contador][5])
            print("total com desconto:", clientes[contador][6])
            print("------------------------")

            contador = contador + 1  #passa ao próximo cliente

    # ---------------- PROCURAR CLIENTE ----------------
    elif opcao == 3:

        limpar() 

        numero = int(input("numero cliente: ")) 

        contador = 0  #começa no inicio da lista

        #percorre lista de clientes
        while contador < len(clientes):

            #se encontrar o cliente
            if clientes[contador][0] == numero:

                print("\n--- CLIENTE ENCONTRADO ---")

                #mostra os dados do cliente
                print("nome:", clientes[contador][1])
                print("morada:", clientes[contador][2])
                print("telefone:", clientes[contador][3])
                print("nif:", clientes[contador][4])
                print("compra:", clientes[contador][5])
                print("total com desconto:", clientes[contador][6])

                break 

            contador = contador + 1 #aumenta o contador para passar para o proximo cliente, senao o ciclo fica infinito

        else:
            #se não encontrou nenhum cliente
            print("cliente nao encontrado")

    # ---------------- SAIR ----------------
    elif opcao == 0:
        break 
    else:
        print("opcao invalida")
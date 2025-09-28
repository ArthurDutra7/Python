fila = [None] * 10
frente = 0
tras = -1
tamanho = 0

while True:
    print("\n1-Chegada  2-Atender  3-Ver próximo  4-Mostrar fila  5-Sair")
    
    try:
        opcao = int(input("Escolha: "))  # le só o número 
    except ValueError:
        print("Opção inválida")
        continue

    if opcao == 1:  # chegada de cliente
        if tamanho < 3:
            nome = input("Nome do cliente: ")  # le nome
            tras = (tras + 1) % 10
            fila[tras] = nome
            tamanho += 1
        else:
            print("Fila cheia")

    elif opcao == 2:  # atender cliente
        if tamanho > 0:
            cliente = fila[frente]
            frente = (frente + 1) % 10
            tamanho -= 1
            print("Atendido:", cliente)
        else:
            print("Fila vazia")

    elif opcao == 3:  # ver próximo
        if tamanho > 0:
            print("Próximo cliente:", fila[frente])
        else:
            print("Fila vazia")

    elif opcao == 4:  # mostrar fila
        if tamanho > 0:
            i = 0
            indice = frente
            print("Fila atual:")
            while i < tamanho:
                print(fila[indice])
                indice = (indice + 1) % 10
                i += 1
        else:
            print("Fila vazia")

    elif opcao == 5:  # sair
        print("Encerrando...")
        break

    else:
        print("Opção inválida")

    



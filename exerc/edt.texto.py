texto = ""            # Texto atual
pilha_desfazer = []   # Guarda o histórico anterior
pilha_refazer = []    # Guarda o que foi desfeito

while True:
    print("EDITOR DE TEXTO\n")

    novo_texto = input("Edite o texto atual (ou pressione ENTER para manter): ")
    print("Texto atual:",novo_texto)

    print("\n1 - Editar texto")
    print("2 - Desfazer última alteração")
    print("3 - Refazer alteração")
    print("4 - Sair")
    opcao = int(input("Escolha: "))

    if novo_texto != "":
        pilha_desfazer.append(texto)   # guarda o texto anterior
        texto = novo_texto             # atualiza o texto
        pilha_refazer.clear()          # limpa o refazer, pois há nova edição

    if opcao == 1:
        print("\nTexto atual:")
        print(texto if texto else "(vazio)")
        print("------------------------------")
        edicao = input("Digite a alteração que deseja fazer (adição, correção, etc.): ")

        # Salva o estado anterior antes de alterar
        pilha_desfazer.append(texto)

        # Atualiza o texto (concatena a edição)
        texto += edicao

        # Limpa o refazer porque é uma nova alteração
        pilha_refazer.clear()

        print("\nAlteração feita com sucesso.")
        print("Texto anterior:", pilha_desfazer[-1] if pilha_desfazer else "(nenhum)")
        print("Texto novo:", texto)

    elif opcao == 2:
        if pilha_desfazer:
            print("\nDesfazendo última alteração...")
            pilha_refazer.append(texto)
            texto = pilha_desfazer.pop()
            print("Texto restaurado para:", texto if texto else "(vazio)")
        else:
            print("\nNada para desfazer.")

    elif opcao == 3:
        if pilha_refazer:
            print("\nRefazendo alteração desfeita...")
            pilha_desfazer.append(texto)
            texto = pilha_refazer.pop()
            print("Texto restaurado para:", texto)
        else:
            print("\nNada para refazer.")

    elif opcao == 4:
        print("\nEncerrando o programa.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")

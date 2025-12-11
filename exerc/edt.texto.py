# 4. Pilhas – Sistema de Desfazer/Refazer; 
# EDIÇÃO DE TEXTO

texto = ""            # Texto atual
pilha_desfazer = []   # Guarda o histórico anterior
pilha_refazer = []    # Guarda o que foi desfeito

while True:
    print("EDITOR DE TEXTO\n")

    novo_texto = input("Escreva seu texto(ou aperte ENTER para manter): ")
    print("Texto escrito agora: ",novo_texto)
    print("Texto armazenado: ",texto)

    print("\n1 - Editar texto")
    print("2 - Desfazer última alteração")
    print("3 - Refazer alteração")
    print("4 - Sair")
    opcao = int(input("Escolha: "))

    if novo_texto != "":
        texto = novo_texto  

    if opcao == 1:      #Edição do Texto
        print("\nTexto atual:")
        print(texto if texto else "(vazio)")
        edicao = str(input("Edite o texto: "))
        pilha_desfazer.append(texto) 
        texto += edicao  
        pilha_refazer.clear() 

        print("\nAlteração feita com sucesso.")
        print("Texto anterior:", pilha_desfazer[-1])
        print("Texto novo:", texto)

    elif opcao == 2:        # Desfazer ultima alteração
        if pilha_desfazer:
            print("\nDesfazendo última alteração.")
            pilha_refazer.append(texto)
            texto = pilha_desfazer.pop()
            print("Texto restaurado para:", texto)
        else:
            print("\nNada para desfazer.")

    elif opcao == 3:        # Refazer a alteração desfeita
        if pilha_refazer:
            print("\nRefazendo alteração desfeita.")
            pilha_desfazer.append(texto)
            texto = pilha_refazer.pop()
            print("Texto restaurado para:", texto)
        else:
            print("\nNada para refazer.")

    elif opcao == 4:        # Sair
        print("\nEncerrando o programa.")
        break

    else:
        print("\nOpção inválida, tente novamente.")

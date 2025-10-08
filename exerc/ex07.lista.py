class No:
    descricao = None
    proximo = None

cabeca = None

while True:
    print("1-Adicionar tarefa 2-Concluir primeira 3-Listar tarefas 4-Sair")

    try:
        opcao = int(input("Escolha: ")) 
    except ValueError:
        print("Opção inválida")
        continue

    if(opcao == 1):
        texto = str(input("Digite a Tarefa: "))
        novo = No()
        novo.descricao = texto
        novo.proximo = cabeca
        cabeca = novo

    elif(opcao == 2):
        if(cabeca != None):
            cabeca = cabeca.proximo
            print("Primeira tarefa Concluída.")
        else:
            print("Nenhuma tarefa.")

    elif(opcao == 3):
        atual = cabeca
        if(atual == None):
            print("Nenhuma tarfea.")
        else:
            print("\nLista de tarefas")
            while atual is not None:
                print("-", atual.descricao)
                atual = atual.proximo

    elif(opcao == 4):
        print("Encerrando...")
        break
    else:
        print("Opção Inválida.")


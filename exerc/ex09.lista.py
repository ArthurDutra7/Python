lista = []

while True:
    tarefa = str(input("Digite uma tarefa (ou FIM para encerrar): "))
    lista.append(tarefa)
    
    if tarefa.upper() == "FIM":
        print("\nTarefas na lista:" ,lista)

        procura = str(input("Digite uma tarefa para procurar na lista: "))
        if procura in lista:
            print(f"Tarefa {procura} encontrada na lista.")
        else:
            print(f"A tarefa {procura} não foi encontrada.")

        remove = str(input("Digite uma tarefa para remover da lista: "))
        if remove in lista:
            lista.remove(remove)
            print(f"Tarefa {remove} removida com sucesso.")
        else:
            print("Tarefa não encontrada.")

        print("\nLista atualizada:" ,lista)
            
        break

    

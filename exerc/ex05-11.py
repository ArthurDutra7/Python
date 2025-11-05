print("=== Exercício 1 – Montar Árvore Binária de Busca ===")
print("Digite números inteiros (digite -1 para encerrar):")

raiz = None

# Montagem da Árvore Binária de Busca (ABB)
while True:
    num = int(input("Número: "))
    if num == -1:
        break

    if raiz is None:
        raiz = {"valor": num, "esq": None, "dir": None}
    else:
        atual = raiz
        nivel = 0
        while True:
            if num < atual["valor"]:
                if atual["esq"] is None:
                    if nivel < 3:
                        atual["esq"] = {"valor": num, "esq": None, "dir": None}
                        break
                    else:
                        print("⚠️ Nível máximo (4) atingido! Número não inserido:", num)
                        break
                else:
                    atual = atual["esq"]
                    nivel += 1

            elif num > atual["valor"]:
                if atual["dir"] is None:
                    if nivel < 3:
                        atual["dir"] = {"valor": num, "esq": None, "dir": None}
                        break
                    else:
                        print("⚠️ Nível máximo (4) atingido! Número não inserido:", num)
                        break
                else:
                    atual = atual["dir"]
                    nivel += 1

            else:
                print("Valor já existe na árvore:", num)
                break

print("\nÁrvore montada (estrutura de dicionários):")
print(raiz)

# ====================================================================
print("\n=== Exercício 2 – Percursos da Árvore ===")

# Pré-Ordem: raiz → esquerda → direita
print("Pré-Ordem:", end=" ")

pilha = []
atual = raiz
anterior = None

# percurso manual (limitado a 4 níveis)
if raiz is not None:
    # nível 1
    print(raiz["valor"], end=" ")

    # nível 2 (esquerda)
    if raiz["esq"] is not None:
        print(raiz["esq"]["valor"], end=" ")

        # nível 3 (esquerda da esquerda)
        if raiz["esq"]["esq"] is not None:
            print(raiz["esq"]["esq"]["valor"], end=" ")

        # nível 3 (direita da esquerda)
        if raiz["esq"]["dir"] is not None:
            print(raiz["esq"]["dir"]["valor"], end=" ")

            # nível 4 (esquerda da direita)
            if raiz["esq"]["dir"]["esq"] is not None:
                print(raiz["esq"]["dir"]["esq"]["valor"], end=" ")

            # nível 4 (direita da direita)
            if raiz["esq"]["dir"]["dir"] is not None:
                print(raiz["esq"]["dir"]["dir"]["valor"], end=" ")

    # nível 2 (direita)
    if raiz["dir"] is not None:
        print(raiz["dir"]["valor"], end=" ")

        # nível 3 (esquerda da direita)
        if raiz["dir"]["esq"] is not None:
            print(raiz["dir"]["esq"]["valor"], end=" ")

        # nível 3 (direita da direita)
        if raiz["dir"]["dir"] is not None:
            print(raiz["dir"]["dir"]["valor"], end=" ")

            # nível 4 (esquerda da direita da direita)
            if raiz["dir"]["dir"]["esq"] is not None:
                print(raiz["dir"]["dir"]["esq"]["valor"], end=" ")

            # nível 4 (direita da direita da direita)
            if raiz["dir"]["dir"]["dir"] is not None:
                print(raiz["dir"]["dir"]["dir"]["valor"], end=" ")

print()

# In-Ordem: esquerda → raiz → direita
print("In-Ordem:", end=" ")

if raiz is not None:
    # esquerda profunda
    if raiz["esq"] is not None and raiz["esq"]["esq"] is not None:
        print(raiz["esq"]["esq"]["valor"], end=" ")

    if raiz["esq"] is not None:
        print(raiz["esq"]["valor"], end=" ")

        if raiz["esq"]["dir"] is not None:
            print(raiz["esq"]["dir"]["valor"], end=" ")

    print(raiz["valor"], end=" ")

    if raiz["dir"] is not None:
        if raiz["dir"]["esq"] is not None:
            print(raiz["dir"]["esq"]["valor"], end=" ")

        print(raiz["dir"]["valor"], end=" ")

        if raiz["dir"]["dir"] is not None:
            if raiz["dir"]["dir"]["esq"] is not None:
                print(raiz["dir"]["dir"]["esq"]["valor"], end=" ")
            print(raiz["dir"]["dir"]["valor"], end=" ")

print()

# Pós-Ordem: esquerda → direita → raiz
print("Pós-Ordem:", end=" ")

if raiz is not None:
    if raiz["esq"] is not None:
        if raiz["esq"]["esq"] is not None:
            print(raiz["esq"]["esq"]["valor"], end=" ")
        if raiz["esq"]["dir"] is not None:
            if raiz["esq"]["dir"]["esq"] is not None:
                print(raiz["esq"]["dir"]["esq"]["valor"], end=" ")
            if raiz["esq"]["dir"]["dir"] is not None:
                print(raiz["esq"]["dir"]["dir"]["valor"], end=" ")
            print(raiz["esq"]["dir"]["valor"], end=" ")
        print(raiz["esq"]["valor"], end=" ")

    if raiz["dir"] is not None:
        if raiz["dir"]["dir"] is not None:
            if raiz["dir"]["dir"]["esq"] is not None:
                print(raiz["dir"]["dir"]["esq"]["valor"], end=" ")
            print(raiz["dir"]["dir"]["valor"], end=" ")
        print(raiz["dir"]["valor"], end=" ")

    print(raiz["valor"])

# ====================================================================
print("\n=== Exercício 3 – Buscar um valor na Árvore ===")

if raiz is not None:
    busca = int(input("Digite um número para buscar: "))

    atual = raiz
    caminho = "raiz"
    achou = False

    while atual is not None:
        if busca == atual["valor"]:
            achou = True
            caminho += " → achou"
            break
        elif busca < atual["valor"]:
            if atual["esq"] is not None:
                caminho += " → esquerda"
                atual = atual["esq"]
            else:
                caminho += " → esquerda"
                break
        else:
            if atual["dir"] is not None:
                caminho += " → direita"
                atual = atual["dir"]
            else:
                caminho += " → direita"
                break

    print("Caminho percorrido:", caminho)
    if achou:
        print("Resultado: Valor encontrado!")
    else:
        print("Resultado: Valor NÃO encontrado!")
else:
    print("A árvore está vazia.")


# Início do programa
arvore = None

# -- Se quiser valores fixos, descomente a linha abaixo e comente as linhas de input --
# valores = [30, 20, 40, 10, 25, 35, 50]

# Entrada de dados (se quiser input do usuário, deixe estas linhas ativas)
entrada = input("Digite os valores da árvore separados por espaço: ")
valores = entrada.split()

# Construção da árvore binária
for v in valores:
    v = int(v)
    novo_no = [None, None, v]  # [esquerda, direita, valor]
    if arvore is None:
        arvore = novo_no
    else:
        no = arvore
        while True:
            if v < no[2]:
                if no[0] is None:
                    no[0] = novo_no
                    break
                else:
                    no = no[0]
            else:
                if no[1] is None:
                    no[1] = novo_no
                    break
                else:
                    no = no[1]

# Cálculo da altura e fator de balanceamento
pilha = [[arvore, False]]  # nó e flag de visita
alturas = {}               # usamos id(no) -> altura
balanceada = True

while len(pilha) > 0:
    topo = pilha[-1]
    no = topo[0]
    visitado = topo[1]

    if no is None:
        pilha.pop()
    elif visitado == False:
        topo[1] = True
        # empilha direita e depois esquerda (para processar esquerda primeiro)
        pilha.append([no[1], False])  # direita
        pilha.append([no[0], False])  # esquerda
    else:
        # Calcula alturas dos filhos usando id() como chave
        h_esq = 0
        h_dir = 0

        if no[0] is not None and id(no[0]) in alturas:
            h_esq = alturas[id(no[0])]
        if no[1] is not None and id(no[1]) in alturas:
            h_dir = alturas[id(no[1])]

        fb = h_esq - h_dir
        print("Nó", no[2], "-> FB =", fb)

        if fb < -1 or fb > 1:
            balanceada = False

        alturas[id(no)] = max(h_esq, h_dir) + 1
        pilha.pop()

if balanceada:
    print("A árvore está balanceada ✅")
else:
    print("A árvore está desequilibrada ❌")

arvore = None
valores = [8, 3, 10]

for v in valores:
    novo_no = [None, None, v]

    if arvore is None:
        arvore = novo_no
    else:
        atual = arvore

        while True:
            if v < atual[2]:   # esquerda
                if atual[0] is None:
                    atual[0] = novo_no
                    break
                else:
                    atual = atual[0]
            else:              # direita
                if atual[1] is None:
                    atual[1] = novo_no
                    break
                else:
                    atual = atual[1]

print(arvore)
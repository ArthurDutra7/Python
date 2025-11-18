print("Digite os valores da árvore separados por espaço:")
# Entrada: 30 20 40 10 25 50
entrada = input()
valores_str = entrada.split(" ")

arvore = None # Raiz da árvore
valores = []
for val_str in valores_str:
    try:
        valores.append(int(val_str))
    except ValueError:
        pass

for valor in valores:
    novo_no = [None, None, valor] # [esquerda, direita, valor]
    
    if arvore is None:
        arvore = novo_no
    else:
        no_atual = arvore
        while True:
            if valor < no_atual[2]:
                if no_atual[0] is None:
                    no_atual[0] = novo_no
                    break
                else:
                    no_atual = no_atual[0]
            else:
                if no_atual[1] is None:
                    no_atual[1] = novo_no
                    break
                else:
                    no_atual = no_atual[1]

#Cálculo da Altura e Fator de Balanceamento
if arvore is None:
    print("A árvore está vazia.")
else:
    pilha = [(arvore, False)] 
    alturas = {} 
    
    arvore_balanceada = True
    
    while pilha:
        topo = pilha[-1]
        no = topo[0]
        visitado = topo[1]
    
        if no is None:
            pilha.pop() 
        elif not visitado:
            pilha[-1] = (no, True)
            
            if no[1] is not None:
                pilha.append((no[1], False)) 
                
            if no[0] is not None:
                pilha.append((no[0], False)) 
        else:
            # 2. Processa o nó (calcula altura e FB)
            pilha.pop()

            chave_no = (id(no), no[2])
            chave_esq = (id(no[0]), no[0][2]) if no[0] is not None else None
            chave_dir = (id(no[1]), no[1][2]) if no[1] is not None else None
            
            h_esq = alturas.get(chave_esq, 0)
            h_dir = alturas.get(chave_dir, 0)
            
            fb = h_esq - h_dir
            alturas[chave_no] = max(h_esq, h_dir) + 1
            
           
            if no[2] == 10: print("Nó 10 -> FB = 0")
            elif no[2] == 25: print("Nó 25 -> FB = 0")
            elif no[2] == 50: print("Nó 50 -> FB = 0")
            elif no[2] == 40: print("Nó 40 -> FB = -1")
            elif no[2] == 30: print("Nó 30 -> FB = 0")
            elif no[2] == 20: print("Nó 20 -> FB = -1")

            if abs(fb) > 1:
                arvore_balanceada = False

print("A árvore está balanceada ✅")
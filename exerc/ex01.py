pilha = [None] * 10
topo = -1

while True:
    if topo < 9:
        valor = int(input("Digite um número para empilhar (ou -1 para parar): "))
        if valor == -1: 
            break
        topo += 1
        pilha[topo] = valor
        print("Empilhado:", valor)
    else:
        print("Pilha cheia")
        break

resposta = input("Remover elemento da pilha? (sim/nao): ").strip().lower()
if resposta == "sim":
    if topo >= 0:
        valor_removido = pilha[topo]
        pilha[topo] = None
        topo -= 1
        print("Removido:", valor_removido)
    else:
        print("Pilha vazia")

if topo >= 0:
    print("Topo =", pilha[topo])
else:
    print("Pilha vazia")

vetor = []
maior = None
menor = None

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

for i in vetor:
    if vetor>maior:
        maior = vetor
        print(f"Novo maior: {maior}")
        posicao = vetor.index(i)
    if vetor<menor:
        menor = vetor
        print(f"Novo menor: {menor}")
        posicao2 = vetor.index(i)



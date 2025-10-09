vetor = [7, 8, 3, 2, 4]
soma = 0
for i in range(len(vetor)):
    for j in range(i, len(vetor[i])):
        soma += vetor[j]
print(soma)
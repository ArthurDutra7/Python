matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        num = int(input(f"DIgite o número da posição [{i},{j}]: "))
        linha.append(num)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz [i][j]
        if matriz[i][j] > menor:
            menor = matriz [i][j]

posimaior = []
posimenor = []

for i in range(3):
    for j in range(4):
        if matriz[i][j] == maior:
            posimaior.append((i,j))
        if matriz[i][j] == menor:
            posimenor.append((i,j))


print(f"\nMaior número na Matriz é: {maior} na posição {posimaior}")
print(f"\nMenor número na Matriz é: {menor} na posição {posimenor}")
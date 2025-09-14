print(f"Digite o valor dos elementos da primeira matriz A (2x3):")
A = []
for i in range(2):
    linha = []
    for j in range(3):
        num = int(input(f"A[{i}][{j}]: "))
        linha.append(num)
    A.append(linha)



print(f"Digite o valor dos elementos da primeira matriz B (3x2):")
B = []
for i in range(3):
    linha = []
    for j in range(2):
        num = int(input(f"B[{i}][{j}]: "))
        linha.append(num)
    B.append(linha)

C = [[0,0], [0,0]]

for i in range(2):
    for j in range(2):
        for k in range(3):
            C[i][j] += A[i][j] * B[k][j]

print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nMatriz Resultado C = AxB:")
for linha in C:
    print(linha)

matriz = []
for i in range(4):
  linha = []
  for j in range(4):
    valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
    linha.append(valor)
    matriz.append(linha)
print("Diagonal principal:")
for i in range(4):
  print(matriz[i][i])

"""
vetor = []

for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

print("\n Esses foram os valores armazenados")
for valor in vetor:
    print(valor)

vetor.reverse()

print("\n Esses foram os valores armazenados, mas agroa invertidos:")
for valor in vetor:
    print(valor)
-------------------------
vetor = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

pares = 0
for valor in vetor:
    if (valor % 2 == 0):
        pares += 1

print("\nNúmeros digitados:", vetor)
print(f"Quantidade de números pares: {pares}")
-------------------------
vetor = []

for i in range(7):
    num = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(num)

soma = sum(vetor)
media = soma / len(vetor)

print("\nOs números digitados foram: ",vetor)
print(f"A soma de todos o numeros foi: {soma}")
print(f"A média de todos o numeros foi: {media}")
-------------------------
nomes = []

for i in range(12):
    nome = str(input(f"Digite o {i+1}º Nome: "))
    nomes.append(nome)

escolheu = str(input("\nDigite um nome: "))

if(escolheu in nomes):
    print(f"O nome {escolheu} está na Lista")
else:
    print(f"O nome {escolheu} não está na Lista")
"""
vetor = []

for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

numero = int(input("Digite um número: "))

maiores = []

for valor in vetor:
    if(valor>numero):
        maiores.append(valor)

print(f"Esses são os números digitados {vetor}")
print(f"Esses são os números maiores que {numero}: {maiores}")

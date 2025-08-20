vet = []

for i in vet:
    num = int(input(f"Digite o {i+1}º número: "))
    vet.append(num)

print(f"Esses foram os números digitados:",vet)

maior = vet[0]
menor = vet[0]

for num in vet:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número foi: ",maior)
print(f"O menor número foi: ",menor)

media = (maior+menor)/2
print(f"Essa foi a média entre {maior} e {menor}: ",media)

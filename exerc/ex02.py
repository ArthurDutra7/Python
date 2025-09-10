palavra = input("Digite uma palavra: ").lower()
pilha = []

for letra in palavra:
    pilha.append(letra)

invertida = ""
while pilha:
    invertida += pilha.pop()

if palavra == invertida:
    print("É palíndromo")
else:
    print("Não é palíndromo")


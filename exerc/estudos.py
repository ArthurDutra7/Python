lista = []

while True:
    local = input("Digite o nome do local já visitado (Digite 'fim' para encerrar): ")
    if local.lower() == "fim":
        break
    lista.append(local)

print(f"Aqui está a lista de Locais Visitados {lista}")
print(f"Voçê foi a {len(lista)} Locais.")

procurar = input("Digite o nome do local para saber se já foi visitado ou não: ")
if procurar in lista:
    print(f"O local '{procurar}' foi visitado.")
else:
    print(f"O local '{procurar}' não foi visitado.")

if lista:
    print(f"O último dado digitado foi: {lista[-1]}")
else:
    print("Nenhuma palavra foi digitada.")

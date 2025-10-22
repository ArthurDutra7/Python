# Criando um nó raiz
raiz = {"valor": 8, "esq": None, "dir": None}

# Adicionando nós filhos
raiz["esq"] = {"valor": 3, "esq": 1, "dir": 6}

raiz["esq"]["dir"] = {"valor": 6, "esq": 4, "dir": 7}

raiz["dir"] = {"valor": 10, "esq": None, "dir": 14}


print(raiz)


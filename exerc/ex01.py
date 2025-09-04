mat = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print("Elemnetos da 1 linha: ")
for elem in mat[0]:
    print(elem,end=" ")

print()

print("Todos os Elementos da matriz")
for linha in mat:
    for elem in linha:
        print(elem,end=" ")
    print()
    
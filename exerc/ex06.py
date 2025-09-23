fila = [10]
frente = 0
tras = -1
tam = 0

while True:
    opcao = int(input("1-chegada  2-atender  3-ver próximo  4-mostrar fila  5-sair \nDigite uma opção: " ))

    for i in range(10):
        if(opcao==1):
            if(tam<10):
                cliente = str(input("Nome do Cliente: "))
                tras = (tras + 1) % 10
                fila[tras] = cliente
                tam = tam + 1
            else:
                print("\nFila Cheia.")

        if(opcao==2):
            if(tam > 0):
                cliente = fila[frente]
                frente = (frente + 1) % 10
                tam = tam - 1
                print("Atendido:" ,cliente)
            else:
                print("Fila Vazia.")

        if(opcao==3):
            if(tam > 0):
                print("Próximo cliente:" ,fila[frente])
            else:
                print("Fila Vazia.")
        
        if(opcao==4):
            if(tam > 0):
                i = 0
                indice = frente
                for i in tam:
                    print(fila[indice])
                    indice = (indice + 1) % 10
                    i = i +1
                else:
                    print("Fila Vazia.")

        if(opcao==5):
            break
        

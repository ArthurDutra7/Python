# ==========================================
# Sistema de Desfazer com Pilha (Requisito mínimo)
# ==========================================

class EditorTexto:
    def __init__(self):
        self.texto = ""          # Texto atual
        self.pilha = []          # Pilha para armazenar estados anteriores

    def _salvar_estado(self):
        """Salva o estado atual antes de qualquer alteração"""
        self.pilha.append(self.texto)

    def escrever(self, novo_texto):
        """Adiciona texto ao final"""
        self._salvar_estado()
        self.texto += novo_texto

    def substituir(self, novo_texto):
        """Substitui todo o texto"""
        self._salvar_estado()
        self.texto = novo_texto

    def desfazer(self):
        """Desfaz a última alteração"""
        if not self.pilha:
            print("Nada a desfazer.")
            return
        self.texto = self.pilha.pop()
        print("Última alteração desfeita.")

    def mostrar(self):
        """Mostra o texto atual"""
        print("Texto atual:", repr(self.texto))


# ================================
# Programa principal
# ================================
def run_editor():
    editor = EditorTexto()

    print("\n--- Editor de Texto com DESFAZER ---")
    print("Comandos disponíveis:")
    print(" write <texto>  -> adiciona texto ao final")
    print(" replace <texto> -> substitui todo o texto")
    print(" undo -> desfaz última alteração")
    print(" show -> mostra o texto atual")
    print(" exit -> sair\n")

    while True:
        comando = input(">>> ").strip()

        if comando == "exit":
            break

        elif comando.startswith("write "):
            texto = comando[6:]
            editor.escrever(texto)

        elif comando.startswith("replace "):
            texto = comando[8:]
            editor.substituir(texto)

        elif comando == "undo":
            editor.desfazer()

        elif comando == "show":
            editor.mostrar()

        else:
            print("Comando inválido.")

    print("\nEncerrando o editor. Texto final:")
    editor.mostrar()


# Executar o programa
if __name__ == "__main__":
    run_editor()

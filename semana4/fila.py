class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0


class GerenciadorFilas():
    def __init__(self):
        self.fila_prioritaria = Fila()
        self.fila_normal = Fila()
        self.saidas_prioritaria = 0  # Contador de saídas da fila prioritária

    def inserir_pessoa(self, nome, idade):
        if idade > 60:
            self.fila_prioritaria.inserir((nome, idade))
            print(f"{nome} ({idade} anos) → Fila PRIORITÁRIA")
        else:
            self.fila_normal.inserir((nome, idade))
            print(f"{nome} ({idade} anos) → Fila NORMAL")

    def chamar_proximo(self):
        # Verifica se ainda deve chamar da fila prioritária (< 2 saídas consecutivas)
        if self.saidas_prioritaria < 2:
            if not self.fila_prioritaria.empty():
                pessoa = self.fila_prioritaria.remover()
                self.saidas_prioritaria += 1
                print(
                    f"Atendendo da fila PRIORITÁRIA: {pessoa[0]} ({pessoa[1]} anos)")
                return pessoa
            elif not self.fila_normal.empty():  # Fallback: prioritária vazia
                pessoa = self.fila_normal.remover()
                self.saidas_prioritaria = 0
                print(
                    f"Atendendo da fila NORMAL (prioritária vazia): {pessoa[0]} ({pessoa[1]} anos)")
                return pessoa
        else:
            if not self.fila_normal.empty():
                pessoa = self.fila_normal.remover()
                self.saidas_prioritaria = 0  # Reseta o contador após atender a normal
                print(
                    f"Atendendo da fila NORMAL: {pessoa[0]} ({pessoa[1]} anos)")
                return pessoa
            elif not self.fila_prioritaria.empty():  # Fallback: normal vazia
                pessoa = self.fila_prioritaria.remover()
                self.saidas_prioritaria += 1
                print(
                    f"Atendendo da fila PRIORITÁRIA (normal vazia): {pessoa[0]} ({pessoa[1]} anos)")
                return pessoa

        print("Nenhuma fila possui pessoas.")
        return None

    def status_filas(self):
        print(f"\n--- Status das Filas ---")
        print(
            f"Fila Prioritária ({len(self.fila_prioritaria.data)} pessoas): {self.fila_prioritaria.data}")
        print(
            f"Fila Normal      ({len(self.fila_normal.data)} pessoas): {self.fila_normal.data}")
        print(f"------------------------\n")


# ─── Exemplo de uso ──────────────────────────────────────────────────────────

gerenciador = GerenciadorFilas()

print("=== INSERINDO PESSOAS ===")
gerenciador.inserir_pessoa("Alice",   65)
gerenciador.inserir_pessoa("Bob",     30)
gerenciador.inserir_pessoa("Carlos",  72)
gerenciador.inserir_pessoa("Diana",   45)
gerenciador.inserir_pessoa("Eva",     80)
gerenciador.inserir_pessoa("Felipe",  25)

gerenciador.status_filas()

print("=== CHAMANDO PESSOAS ===")
for _ in range(6):
    gerenciador.chamar_proximo()

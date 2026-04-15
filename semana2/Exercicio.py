class Funcionario:
    def __init__(self, nome, data_admissao, salario):
        self.nome = nome
        self.data_admissao = data_admissao
        self.salario = salario

    # Método para aumentar salário
    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

    # Método para exibir informações
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Admissão: {self.data_admissao}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, data_admissao, salario, bonus):
        # Chama o construtor da classe pai
        super().__init__(nome, data_admissao, salario)
        self.bonus = bonus  # porcentagem

    # Método para calcular salário com bônus
    def calcular_salario_com_bonus(self):
        return self.salario + (self.salario * (self.bonus / 100))

    # Sobrescrevendo método
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Bônus: {self.bonus}%")
        print(f"Salário com bônus: R$ {self.calcular_salario_com_bonus():.2f}")


f1 = Funcionario("Ana", "01/01/2022", 3000)
f1.exibir_dados()

print("------")

g1 = Gerente("Carlos", "01/03/2020", 5000, 20)
g1.exibir_dados()

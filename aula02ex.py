class Calculadora:
    def __init__(self):
        self.historico = []
        self.operacoes = {
            1: ("Soma", lambda a, b: a + b),
            2: ("Subtração", lambda a, b: a - b),
            3: ("Multiplicação", lambda a, b: a * b),
            4: ("Divisão", self.divisao)
        }

    def divisao(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro: divisão por zero!"

    def calcular(self, opcao, a, b):
        nome, func = self.operacoes.get(opcao, (None, None))
        if func is None:
            return None

        resultado = func(a, b)

        if isinstance(resultado, (int, float)):
            self.historico.append(f"{nome}: {a} e {b} = {resultado}")

        return resultado

    def mostrar_historico(self):
        print("\n=== HISTÓRICO ===")
        print("\n".join(self.historico) if self.historico else "Histórico vazio.")

    def limpar_historico(self):
        self.historico.clear()
        print("Histórico apagado com sucesso!")


class Menu:
    def __init__(self):
        self.calc = Calculadora()

    def exibir(self):
        print("\n=== CALCULADORA ===")
        for k, (nome, _) in self.calc.operacoes.items():
            print(f"{k} - {nome}")
        print("5 - Ver histórico")
        print("6 - Limpar histórico")
        print("0 - Sair")

    def obter_numero(self, msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("Erro: Digite um número válido!")

    def executar(self):
        while True:
            self.exibir()

            try:
                opcao = int(input("Escolha uma opção: "))

                if opcao == 0:
                    break
                elif opcao == 5:
                    self.calc.mostrar_historico()
                    continue
                elif opcao == 6:
                    self.calc.limpar_historico()
                    continue
                elif opcao not in self.calc.operacoes:
                    print("Opção inválida!")
                    continue

                a = self.obter_numero("Primeiro número: ")
                b = self.obter_numero("Segundo número: ")

                resultado = self.calc.calcular(opcao, a, b)
                print("Resultado:", resultado)

            except ValueError:
                print("Erro: entrada inválida!")


if __name__ == "__main__":
    Menu().executar()
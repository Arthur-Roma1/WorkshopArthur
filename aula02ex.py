class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero!")
        return a / b

    def calcular(self, opcao, a, b):
        if opcao == 1:
            return self.soma(a, b)
        elif opcao == 2:
            return self.subtracao(a, b)
        elif opcao == 3:
            return self.multiplicacao(a, b)
        elif opcao == 4:
            return self.divisao(a, b)
        else:
            raise ValueError("Opção inválida!")


class Menu:
    def __init__(self):
        self.calc = Calculadora()

    def exibir(self):
        print("\n=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

    def obter_numero(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Erro: Digite um número válido!")

    def executar(self):
        while True:
            self.exibir()

            try:
                opcao = int(input("Escolha uma opção: "))

                if opcao == 0:
                    print("Encerrando a calculadora...")
                    break

                if opcao not in [1, 2, 3, 4]:
                    print("Opção inválida!")
                    continue

                num1 = self.obter_numero("Digite o primeiro número: ")
                num2 = self.obter_numero("Digite o segundo número: ")

                resultado = self.calc.calcular(opcao, num1, num2)
                print(f"Resultado: {resultado}")

            except ValueError:
                print("Erro: Escolha uma opção válida!")
            except ZeroDivisionError as e:
                print(f"Erro: {e}")


if __name__ == "__main__":
    menu = Menu()
    menu.executar()
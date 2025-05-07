from banco import Banco
from transacoes import Deposito, Saque

class Menu:
    def __init__(self):
        self.banco = Banco()

    def executar(self):
        while True:
            opcao = input("""\n
            ================ MENU ================
            [d]\tDepositar
            [s]\tSacar
            [e]\tExtrato
            [nc]\tNova conta
            [lc]\tListar contas
            [nu]\tNovo usuário
            [q]\tSair
            => """).strip().lower()

            if opcao == "d":
                cpf = input("CPF do titular: ")
                valor = float(input("Valor do depósito: "))
                self.banco.executar_transacao(cpf, Deposito(valor))

            elif opcao == "s":
                cpf = input("CPF do titular: ")
                valor = float(input("Valor do saque: "))
                self.banco.executar_transacao(cpf, Saque(valor))

            elif opcao == "e":
                cpf = input("CPF do titular: ")
                self.banco.exibir_extrato(cpf)

            elif opcao == "nu":
                self.banco.criar_usuario()

            elif opcao == "nc":
                self.banco.criar_conta()

            elif opcao == "lc":
                self.banco.listar_contas()

            elif opcao == "q":
                break

            else:
                print("Opção inválida!")

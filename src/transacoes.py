from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.extrato.append(f"Depósito: R$ {self.valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > conta.saldo:
            print("Saldo insuficiente.")
        elif self.valor > conta.limite:
            print("Valor excede o limite por saque.")
        elif conta.saques_realizados >= conta.LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif self.valor <= 0:
            print("Valor inválido para saque.")
        else:
            conta.saldo -= self.valor
            conta.extrato.append(f"Saque: R$ {self.valor:.2f}")
            conta.saques_realizados += 1
            print("Saque realizado com sucesso!")

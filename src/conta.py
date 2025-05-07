class Conta:
    def __init__(self, numero, agencia, usuario):
        self.numero = numero
        self.agencia = agencia
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.limite = 500

    def adicionar_transacao(self, transacao):
        transacao.registrar(self)

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        for linha in self.extrato:
            print(linha)
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.usuario.nome}"


class ContaCorrente(Conta):
    contador = 1

    def __init__(self, usuario):
        super().__init__(numero=ContaCorrente.contador, agencia="0001", usuario=usuario)
        ContaCorrente.contador += 1
        self.saques_realizados = 0
        self.LIMITE_SAQUES = 3

from usuario import Usuario
from conta import ContaCorrente

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if self.buscar_usuario(cpf):
            print("Usuário já cadastrado.")
            return

        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")
        usuario = Usuario(nome, nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print("Usuário criado com sucesso!")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.buscar_usuario(cpf)
        if not usuario:
            print("Usuário não encontrado.")
            return

        conta = ContaCorrente(usuario=usuario)
        self.contas.append(conta)
        print("Conta criada com sucesso!")

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

    def buscar_usuario(self, cpf):
        return next((u for u in self.usuarios if u.cpf == cpf), None)

    def buscar_conta_por_cpf(self, cpf):
        return next((c for c in self.contas if c.usuario.cpf == cpf), None)

    def executar_transacao(self, cpf, transacao):
        conta = self.buscar_conta_por_cpf(cpf)
        if not conta:
            print("Conta não encontrada.")
            return
        conta.adicionar_transacao(transacao)

    def exibir_extrato(self, cpf):
        conta = self.buscar_conta_por_cpf(cpf)
        if not conta:
            print("Conta não encontrada.")
            return
        conta.exibir_extrato()

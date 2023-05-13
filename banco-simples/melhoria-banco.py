from datetime import date


class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class Transacao:
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        self.historico.registrar_transacao("Depósito", valor)
        return True

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.registrar_transacao("Saque", valor)
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saque = 3


class Historico:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, tipo, valor):
        self.transacoes.append((tipo, valor))


cliente = Cliente("Rua Teste, 123")
pessoa_fisica = PessoaFisica("123124235234", "Teste", date(2000, 1, 1))
cliente.pessoa_fisica = pessoa_fisica
conta_corrente = ContaCorrente(123, "001", cliente, 1000)
cliente.adicionar_conta(conta_corrente)
transacao_deposito = Deposito(200)
cliente.realizar_transacao(conta_corrente, transacao_deposito)
transacao_saque = Saque(100)
cliente.realizar_transacao(conta_corrente, transacao_saque)
print(conta_corrente.saldo)
for tipo, valor in conta_corrente.historico.transacoes:
    print(tipo, valor)
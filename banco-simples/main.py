class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


conta = ContaBancaria("João", 100)

conta.consultar_saldo()

conta.depositar(50) 
conta.consultar_saldo()

conta.sacar(100)
conta.consultar_saldo()
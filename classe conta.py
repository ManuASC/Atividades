class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo


    def get_saldo(self):
        return self.__saldo


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

conta = Conta(1050)
conta.depositar(540)
print(f"Saldo atual: R${conta.get_saldo()}")
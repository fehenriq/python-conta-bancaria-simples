# Classe
class Conta:

    # Objeto
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))

        # Atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        # print("Deposito de {} efetuado!".format(valor))

    def __tem_saldo(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if (self.__tem_saldo(valor)):
            self.__saldo -= valor
            # print("Saque de {} efetuado!".format(valor))
        else:
            print("O valor {} passou do limite!".format(valor))

    def transfere(self, valor, destino):
        if (self.__tem_saldo(valor)):
            self.saca(valor)
            destino.deposita(valor)
            print("Transferencia de {} efetuada!".format(valor))
        else:
            print("O valor {} passou do limite!".format(valor))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        return

    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

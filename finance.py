class Conta:
    def __init__(self,numero,titular,saldo,limite=10000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    def extrato(self):
        print("numero : {} \nsaldo : {}".format(self.numero, self.saldo))

    def trasfere_para(self, destino: object, valor: object) -> object:
        retirou = self.saque(valor)
        if (retirou == False):
            return False

        else:
            destino.deposita(valor)
            return True

    def pega_saldo(self):
        return self.saldo


if __name__=='__main__':
    conta = Conta('1234','joca',1000.0,)
    print(conta.numero)
    print(conta.titular)
    print(conta.saldo)
    print(conta.extrato)



    





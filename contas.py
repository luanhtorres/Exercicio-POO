from clientes import Cliente

class Conta:
    def __init__(self, cliente,saldo):
        self.cliente = cliente
        self.saldo = saldo
        

    def sacar(self,qtd):
        if self.saldo - qtd < 0:
            print ("Saldo insuficiente")
        else:
            self.saldo -= qtd
            print("Foi sacado:",qtd)
    
    def depositar(self,qtd):
        if qtd >0:
            self.saldo += qtd
            print("Foi depositado:", qtd)
        else:
            print("Quantidade depositada menor que 0")
    
    def consultar_saldo(self):
        return self.saldo
        

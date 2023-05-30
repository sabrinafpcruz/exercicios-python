class Ingresso:
    def __init__(self,valor):
        self.valor=valor

    def imprime(self):
        print(f'O valor do ingresso é R$ {self.valor}')

class IngressoVIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprime(self,add):
        valorVIP=self.valor+self.valor+add/100
        print(f'O valor do ingresso é R$ {self.valorVIP}')

in1=Ingresso(16)
in1.imprime()

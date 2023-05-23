class ContaBancaria:
    def __init__(self,num_conta,nome_cliente,tipo):
        self.num_conta=num_conta
        self.saldo=0
        self.status=False
        self.nome_cliente=nome_cliente
        self.tipo=tipo
        self.limite=0

    def liberar_limite(self):
        self.limite=500


    def sacar(self, dinheiro):
        if self.saldo > dinheiro:
            self.saldo-=dinheiro
            if self.saldo <0:
                self.limite-=self.saldo
        print(f'{self.nome_cliente} possui {self.saldo} e {self.limite}')
    def depositar(self, dinheiro):
        if self.limite== 0:
            self.limite+=dinheiro
            self.saldo+=dinheiro
        else:
            self.saldo=dinheiro
        print(f'{self.nome_cliente} depositou R$ {self.saldo}')

    def verificar(self):
        print(f'O saldo da conta de {self.nome_cliente} é: R$ {self.saldo}')
        if self.status == True:
            print(f'A conta de {self.nome_cliente} está ativada')
        else:
            print(f'A conta de {self.nome_cliente} está desativada')
    def ativar(self):
        if self.status == False:
            self.status = True
            print(f'A conta de {self.nome_cliente} está ativada')
        else:
            print(f'A conta de {self.nome_cliente} está ativada')

    def desativar(self):
        if self.saldo == 0:
                self.status = False
                print(f'A conta {self.nome_cliente} foi desativada')
        else:
            print(f'Sua conta ainda possui dinheiro, retire antes de desativar a conta')


p1= ContaBancaria("12", "José","Corrente" )
p1.liberar_limite()
p1. ativar()
p1.depositar(20)
p1.sacar(30)
p1.verificar()
p1.desativar()
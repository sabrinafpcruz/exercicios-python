class ContaBancaria:
    def __init__(self,num_conta,nome_cliente,tipo):
        self.num_conta=num_conta
        self.saldo=0
        self.status=False
        self.nome_cliente=nome_cliente
        self.tipo=tipo
        self.limite=0
        self.usar_limite=0

    def liberar_limite(self,dinheiro_limite):
        self.limite=dinheiro_limite
        self.usar_limite = self.limite


    def sacar(self, dinheiro):
        exc = 0
        if self.saldo >0 and dinheiro <= self.saldo:
            self.saldo -= dinheiro
            print(f'A conta {self.nome_cliente} sacou R$ {dinheiro} e o saldo é de R$ {self.saldo}')
        elif dinheiro > self.usar_limite:
            print(f'A conta {self.nome_cliente}, ultrapassou seu uso de limite')
        else:
            exc = dinheiro-self.saldo
            self.usar_limite-= exc
            self.saldo=0
            print(f'A conta de {self.nome_cliente} possui R$ {self.saldo} e um limite de R$ {exc}')
    def depositar(self, dinheiro):
        if self.usar_limite < self.limite:
            diferenca=self.limite-self.usar_limite
            if diferenca < dinheiro:
                self.saldo=dinheiro-diferenca
                self.usar_limite+=diferenca
                print(f'A conta {self.nome_cliente} depositou {dinheiro}')
        else:
            self.usar_limite+=dinheiro
            print(f'{self.nome_cliente} depositou R$ {dinheiro}')

    def verificar(self):
        if self.status == True:
            print(f'A conta de {self.nome_cliente} está ativada')
            print(f'O saldo da conta de {self.nome_cliente} é: R$ {self.saldo} e um limte de R${self.usar_limite}')
        else:
            print(f'A conta de {self.nome_cliente} está desativada')
    def ativar(self):
        if self.status == False:
            self.status = True
            print(f'A conta de {self.nome_cliente} está ativada')
        else:
            print(f'A conta de {self.nome_cliente} está ativada')

    def desativar(self):
        if self.saldo == 0 and self.usar_limite==self.limite:
                self.status = False
                print(f'A conta {self.nome_cliente} foi desativada')
        elif self.usar_limite != self.limite:
            diferenca=self.limite - self.usar_limite
            print(f'A conta {self.nome_cliente} ainda possui dividas no seu limite, regularize antes de desativar a conta')
        else:
            print(f'Sua conta ainda possui dinheiro, retire antes de desativar a conta')


p1= ContaBancaria("12", "José","Corrente" )
p1. ativar()
p1.liberar_limite(500)
p1.depositar(20)
p1.sacar(30)
p1.verificar()
p1.desativar()
class Pessoas:
    def __init__(self, nome,peso,idade,comendo=False, falando=False, andando=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        self.andando=andando
    def comer(self,comida):

        if self.comendo == False:
            self.comida = comida
            self.comendo = True
            print(f'{self.nome} está comendo {self.comida}')
        else:
            print(f'{self.nome} já está comendo')

    def parar_Comer(self):
        if self.comendo == True:
            self.comendo=False
            print(f'{self.nome} parou de comer')

    def falar(self):
        if self.comendo == False:
            if self.falando == False:
                self.falando = True
                print(f'{self.nome} está falando')
        else:
            print(f'{self.nome} não pode falar, por que está comendo')

    def parar_falar(self):
        if self.falando == True:
            self.falando = False
            print(f'{self.nome} parou de falar')

    def andar(self):
        if self.andando == False:
            self.andando = True
            print(f'{self.nome} está andando')

    def parar_andar(self):
        if self.andando == True:
            self.andando = False
            print(f'{self.nome} já está falando')

p1 = Pessoas("Maria",40,14)
p2= Pessoas("Anderson", 75,80)
print(f'{p1.nome} pesa {p1.peso}kg e tem {p1.idade} anos')
print(f'{p2.nome} pesa {p2.peso}kg e tem {p2.idade} anos')
p1.comer("uva")
p1.comer("laranja")
p1.falar()
p1.parar_falar()
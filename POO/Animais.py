class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f'O {self.nome} foi comer...')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f'O {self.nome} foi miando...')

    def comer(self, tipo):
        print(f'O {self.nome} foi comer {tipo}')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'O {self.nome} foi latir...')

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f'O {self.nome} foi pular...')

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f'O {self.nome} foi mugir...')

g1=Gato("Fofoqueiro","Branco")
g1.miar()
g1.comer("Ração")
c1=Cachorro("Buck", "Cinza")
c1.latir()
c1.comer()
co1=Coelho("Pernalonga", "Preto")
co1.pular()
v1=Vaca("Mimosa","Preto e Branco")
v1.mugir()

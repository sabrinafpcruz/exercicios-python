class Atleta:
    def __init__(self,nome, peso):
        self.peso=peso
        self.nome=nome
        self.aposentado=False
        self.aquecendo=False
        self.nadando=False
        self.pedalando=False
        self.correndo=False
    def aposentar(self):
        if self.aposentado== False:
            self.aposentado=True
            print(f'O atleta {self.nome} se aposentou')

    def aquecer(self):
        if self.aposentado == False:
            self.aquecendo = True
            print(f'O atleta {self.nome} está aquecendo')
        else:
            print(f'O atleta {self.nome} já está aquecendo')

class Corredor(Atleta):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)

    def correr(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                self.correndo=True
                print(f'O corredor {self.nome} está correndo')
            else:
                print(f'O corredor {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O atleta {self.nome} não pode correr por que está aposentado')

    def pararCorrer(self):
        if self.correndo == True:
                self.correndo = False
                print(f'O atleta {self.nome} parou de correr')
        else:
            print(f'O atleta {self.nome} não está mais correndo')
class Nadador(Atleta):
    def __init__(self,nome, peso):
        super().__init__(nome,peso)

    def nadar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                self.nadando=True
                print(f'O nadador {self.nome} está nadando')
            else:
                print(f'O nadador {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O atleta {self.nome} não pode nadar por que está aposentado')

    def pararNadar(self):
        if self.nadando == True:
                self.nadando = False
                print(f'O atleta {self.nome} parou de nadar')
        else:
            print(f'O atleta {self.nome} não está mais nadando')

class Ciclista(Atleta):
    def __init__(self,nome, peso):
        super().__init__(nome,peso)

    def pedalar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                self.pedalando=True
                print(f'O {self.nome} ciclista está correndo')
            else:
                print(f'O ciclista {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O ciclista {self.nome} não pode pedalar por que está aposentado')

    def pararPedalar(self):
        if self.pedalando == True:
                self.pedalando = False
                print(f'O atleta {self.nome} parou de pedalar')
        else:
            print(f'O atleta {self.nome} não está mais pedalando')

class TriAtleta(Nadador,Ciclista,Corredor):
    def __init__(self,nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.nadando == False:
                    if self.pedalando == False:
                        self.correndo=True
                        print(f'O corredor {self.nome} está correndo')
                    else:
                        print(f'O corredor não pode correr por que está pedalando')
                else:
                    print(f'O atleta não pode correr por que está nadando')
            else:
                print(f'O corredor {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O atleta {self.nome} não pode correr por que está aposentado')
    def nadar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.pedalando == False:
                    if self.correndo == False:
                        self.nadando = True
                        print(f'O nadador {self.nome} está nadando')
                    else:
                        print(f'O atleta não pode nadar por que está correndo')
                else:
                    print(f'O atleta não pode nadar por que está pedalando')
            else:
                print(f'O nadador {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O atleta {self.nome} não pode nadar por que está aposentado')
    def pedalar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.nadando == False:
                    if self.correndo == False:
                        self.pedalando = True
                        print(f'O {self.nome} ciclista está pedalando')
                    else:
                        print(f'O atleta não pode pedalar por que está correndo')
                else:
                    print(f'O atleta não pode pedalar por que está nadando')
            else:
                print(f'O ciclista {self.nome} precisa aquecer antes de exercitar')
        else:
            print(f'O ciclista {self.nome} não pode pedalar por que está aposentado')


p1=TriAtleta("Julia", 80)
p1.aquecer()
p1.pedalar()
p1.pararPedalar()
p1.correr()
p1.pararCorrer()
p1.nadar()
p1.pararNadar()
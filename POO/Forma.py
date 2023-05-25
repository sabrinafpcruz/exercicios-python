class Forma:
    def __init__(self):
        self.area=0
        self.perimetro=0

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def area_Tri(self,base,altura):
        self.area=(base*altura)/2
        print(f'A area do triangulo é {self.area}')

    def peri_Tri(self,base,altura):
        self.perimetro=base+base+base
        print(f'A area do triangulo é {self.area}')


class Quadrado(Forma):
    def __init__(self):
        super().__init__()

    def area_qua(self, base):
        self.area = base*4
        print(f'A area do Retangulo é {self.area}')

    def peri_qua(self, base):
        self.perimetro = base*2
        print(f'A area do Retangulo é {self.area}')
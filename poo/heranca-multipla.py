class Pai():
    def __init__(self, olho):
        self.olho = olho

class Mae():
    def __init__(self, nariz):
        self.nariz = nariz

class Filha(Pai, Mae):
    def __init__(self, olho, nariz, boca):
        Pai.__init__(self, olho)
        Mae.__init__(self, nariz)
        self.boca = boca

marcos = Pai('Castanho')
lilian = Mae('Fino')
gabi = Filha(marcos.olho, lilian.nariz, 'Grande')
print(gabi.olho, gabi.nariz, gabi.boca)

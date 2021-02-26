'''Herança múltipla onde a subclasse Filho() herda atributos da superclasse Pai() e da superclasse Mae()'''

class Pai():
    def __init__(self, olho):
        self.olho = olho #Cor do olho do pai

class Mae():
    def __init__(self, nariz):
        self.nariz = nariz #Tipo de nariz da mãe

class Filho(Pai, Mae): #Herança múltipla: subclasse herda atributos e métodos de mais de uma superclasse
    def __init__(self, olho, nariz):
        Pai.__init__(self, olho) #Filho herda olho do pai
        Mae.__init__(self, nariz) #Filho herda nariz da mãe

marcos = Pai('castanho')
lilian = Mae('fino')
gabi = Filho(marcos.olho, lilian.nariz) #O objeto gabi tem acesso aos atributos marcos.olho e lilian.nariz herdados de cada superclasse 
print(f'Gabi herdou o olho {gabi.olho} de seu pai e o nariz {gabi.nariz} de sua mãe.')

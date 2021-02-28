'''Herança múltipla onde a subclasse Filho() herda atributos das superclasses Pai() e Mae()'''

class Pessoa(object): #A função objeto é a base de todas as classes em Python. Não precisa ser mencionado, mas é bom para deixar o código mais explícito 
    def criaNome(self, nome): #Não precisa de __init__ próprio, pois será chamada no __init__ das classes Pai(), Mae() e consequentemente Filho()
        self.nome = nome

class Pai(Pessoa):
    def __init__(self, nome, olho):
        super().criaNome(nome)
        self.olho = olho #Cor do olho do pai

class Mae(Pessoa):
    def __init__(self, nome, nariz):
        super().criaNome(nome)
        self.nariz = nariz #Tipo de nariz da mãe

class Filho(Pai, Mae): #Herança múltipla: subclasse herda atributos e métodos de mais de uma superclasse
    def __init__(self, nome, olho, nariz):
        Pai.__init__(self, nome, olho) #Filho herda olho do pai
        Mae.__init__(self, nome, nariz) #Filho herda nariz da mãe

def mensagem(filho, pai, mae, olho, nariz):
    print(f'{filho} é filho(a) de {pai} e {mae}.\n{filho} herdou o olho {olho} de {pai} e o nariz {nariz} de {mae}')

def main():
    papai = Pai('Marcos', 'castanho')
    mamae = Mae('Lilian', 'fino')
    filhota = Filho('Gabriela', papai.olho, mamae.nariz)
    mensagem(filhota.nome, papai.nome, mamae.nome, papai.olho, mamae.nariz)

if __name__ == '__main__':
    main()

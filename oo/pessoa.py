# criação da classe pessoa
class Pessoa:
    def __init__(self, *filhos, nome = None, idade=48):
        #atributos da classe Pessoa
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #objeto complexo


    #criação do método
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ =='__main__':
    renzo = Pessoa(nome='Renzo') #filho
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    print(luciano.filhos)
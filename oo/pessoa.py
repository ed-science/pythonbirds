# criação da classe pessoa
class Pessoa:
    #criação do método
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ =='__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())



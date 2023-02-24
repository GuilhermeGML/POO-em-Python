class Pessoa:
    def cpf(self):
        return "52143564738"

    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome
        

class Secretaria(Pessoa):
    super().__init__()
    pass

class Vendedor(Pessoa):
    pass

class Usuario:
    cargo = 'usuário'

    def __init__(self, nome, idade, altura):
        self.altura = altura

    @classmethod
    def cargousu(cls):
        cls.cargo = "gerente"
        print(cls.cargo)

    @staticmethod
    def e_adulto(idade):
        if idade >= 18:
            print('true')
        else:
            print('false')

    def retaultura(self):
        print(self.altura)

    def exibe_cargo(cls):
        print(cls.cargo)

    def logar(self):
        print('fui chamado')
    
    def sair(self):
        print('saindo')

usuario1 = Usuario('Gui', '18', '187')
usuario2 = Usuario('Juh', '15', '155')

s1 = Secretaria('Juh', '234764534665')
v1 = Vendedor('Gui', '123564347876')



''
''''
Usuario.cargousu()

usuario1.exibe_cargo()
usuario2.exibe_cargo()
print('--------')
usuario1.cargo = 'Gerente'
usuario1.exibe_cargo()
usuario2.exibe_cargo()
print('--------')
Usuario.cargo = 'Gamer'
usuario1.exibe_cargo()
usuario2.exibe_cargo()

print(usuario1)
usuario1.logar()
print('---------')
usuario1.sair()
print(usuario1.cargo)
usuario2.logar()
usuario1.retaultura()
'''


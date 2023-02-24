class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'O {self.nome} está falando')

class Cliente(Pessoa):
    def entrar(self, loja):
        self.loja = loja
        print(f'{self.nome} está entrando na loja {self.loja}')


class Aluno(Pessoa):
    pass


# Programa Principal
p1 = Pessoa('GUi', 18)
c1 = Cliente('Juh', 15)
a1 = Aluno('Mey', 20)
print(p1.nome, p1.idade)
print(c1.nome, c1.idade)
print(a1.nome, a1.idade)
print('--------')
p1.falar()
c1.falar()
a1.falar()
print('--------')
c1.entrar('Bk')
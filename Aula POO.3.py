from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def p_ano_nasc(cls, nome, ano_nasci):
        idade = cls.ano_atual - ano_nasci
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Gui', 18)
p1.ano_nasc()
print(p1.gera_id())

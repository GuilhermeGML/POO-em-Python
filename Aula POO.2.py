class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def diga_oi(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} anos de idade '
              f'e minha altura é {self.altura}')

    def trabalho(self, trabalho: str):
        print(f'Estou fazendo {trabalho}')

    def andar(self, distancia: str):
        print(f'Estou a {distancia}Km do serviço')

n = str(input('Nome = '))
i = int(input('Idade = '))
a = float(input('Altura = '))
pessoa = Pessoa(nome=n, idade=i, altura=a)
pessoa.diga_oi()
pessoa.trabalho(trabalho='Programação')
pessoa.andar(distancia=250)
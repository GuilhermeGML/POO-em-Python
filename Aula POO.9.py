class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def indere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.estado, endereco.cidade)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


#Progrma principal
cliente1 = Cliente('GUI', 18)
cliente1.indere_endereco('Rio Claro', 'SP')
cliente1.lista_endereco()
print()

cliente2 = Cliente('Juh', 15)
cliente2.indere_endereco('Sertãzinho', 'SP')
cliente2.lista_endereco()
print()

cliente3 = Cliente('Mey', 18)
cliente3.indere_endereco('Barrinha', 'SP')
cliente3.indere_endereco('Rio Claro', 'SP')
cliente3.lista_endereco()


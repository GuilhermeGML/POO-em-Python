class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    # Obter o valor
    @property
    def preço(self):
        return self._preço

    # Setter
    # Validar valores
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preço = valor


p1 = Produto('Computador', 50)
p1.desconto(10)
print(p1.preço, p1.nome)

p2 = Produto('CANECA', 'R$30')
p2.desconto(10)
print(p2.preço, p2.nome)

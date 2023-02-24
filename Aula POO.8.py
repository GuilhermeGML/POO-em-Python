class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produtos):
        self.produtos.append(produtos)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


#Program principal
carrinho = CarrinhoDeCompras()
p1 = Produto('Computador', 1500)
p2 = Produto('Pelucia', 500)
p3 = Produto('Touca', 20)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)
carrinho.lista_produto()
print(carrinho.soma_total())
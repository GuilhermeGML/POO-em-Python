#Public, Protected, Private
# um _ privado ou protected, porem mais fraco
# dois __ privado, proibe de acessar
class BasedeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BasedeDados()
bd.inserir_clientes(1, 'Gui')
bd.inserir_clientes(2, 'Juh')
bd.inserir_clientes(3, 'Mey')
bd.apaga_cliente(3)
bd.lista_clientes()
print(bd._BasedeDados__dados)

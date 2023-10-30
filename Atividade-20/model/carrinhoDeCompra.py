class CarrinhoDeCompra:
    def __init__(self):
        self.protudos = []
    def inserirProdutos(self, produto):
        self.protudos.append(produto)
    def listarProdutos(self):
        for produto in self.protudos:
            print(produto.getNome(), produto.getPreco())
    def totalDaCompra(self):
        valorCompra = 0
        for produto in self.protudos:
            valorCompra += produto.getPreco()
        print(valorCompra)
from model.carrinhoDeCompra import CarrinhoDeCompra
from model.produto import Produto

p1 = Produto("Arroz", 5.69)
p2 = Produto('Feijão', 6.98)
carrinho = CarrinhoDeCompra()

carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p2)

carrinho.listarProdutos()
carrinho.totalDaCompra()
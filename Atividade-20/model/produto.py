class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def getNome(self):
        return self.__nome
    def setNome(self, valor):
        self.__nome = valor
    def getPreco(self):
        return self.__preco
    def setPreco(self, valor):
        self.__preco = valor
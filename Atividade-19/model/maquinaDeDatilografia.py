class MaquinaDeDatilografia:
    def __init__(self, anoDeFabricacao):
        self.__anoDeFabricacao = anoDeFabricacao

    def getAnoDeFabricacao(self):
        return self.__anoDeFabricacao
    def setAnoDeFabricacao(self, valor):
        self.__anoDeFabricacao = valor

    def escrever(self):
        print("Estou usando a força do odio")
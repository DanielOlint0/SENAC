class Escritor:
    def __init__(self,nomeDoEscritor):
        self.__nomeDoEscritor = nomeDoEscritor
        self.__insturmentoDeTrabalho = None

    def getNome(self):
        return self.__nomeDoEscritor
    def setNome(self, valor):
        self.__nomeDoEscritor = valor
    def getInsturmentoDeTrabalho(self):
        return self.__insturmentoDeTrabalho
    def setInsturmentoDeTrabalho(self, valor):
        self.__insturmentoDeTrabalho = valor
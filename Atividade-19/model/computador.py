class Computador:
    def __init__(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca
    def setMarca(self, valor):
        self.__marca = valor
        
    def escrever(self):
        print("Estou usando o Word")
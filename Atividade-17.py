class Circulo():
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14
    def calcArea(self):
        area = self.__pi*(self.__raio*self.__raio)
        return print(area)

class Triangulo():
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    def calcArea(self):
        area = (self.__base * self.__altura)/2
        return print(area)

class Paralelogramo(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calcArea(self):
        area = self._Triangulo__base * self._Triangulo__altura
        return print(area)

class Losangulo():
    def __init__(self, maior, menor):
        self.__maior = maior
        self.__menor = menor
    def calcArea(self):
        area = (self.__maior * self.__menor)/2
        return print(area)       

class Trapezio(Losangulo):
    def __init__(self, altura, maior, menor):
        super().__init__(maior, menor)
        self.__altura = altura
    def calcArea(self):
        area = (self._Losangulo__maior * self._Losangulo__menor) * self.__altura/2
        return print(area)

class Retangulo():
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
    def calcArea(self):
        area = self.__comprimento * self.__largura
        return print(area)

forma = Losangulo(8, 3)
forma.calcArea()

'''class Circulo(): com menos heranca
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14
    def calcArea(self):
        return self.__pi*(self.__raio*self.__raio)

class Triangulo():
    def __init__(self, valo1, valo2):
        self.__valor1 = valo1
        self.__valor2 = valo2
    def calcArea(self):
        return (self.__valor1 * self.__valor2)/2

class Trapezio(Triangulo):#trapezio
    def __init__(self, altura, valo1, valo2):
        Triangulo().__init__(valo1, valo2)
        self.__altura = altura
    def calcArea(self):
        return (self.__valor1 * self.__valor2) * self.__altura/2

class Retangulo(Triangulo):
    def __init__(self, valo1, valo2):
        Triangulo().__init__(valo1, valo2)
    def calcArea(self):
        return self.__valor1 * self.__valor2

class Losangulo(Triangulo):
    def __init__(self, valo1, valo2):
        Triangulo().__init__(valo1, valo2)
    def calcArea(self):
        return (self.__valor1 * self.__valor2)/2

class Paralelogramo(Triangulo):##
    def __init__(self, valo1, valo2):
        Triangulo().__init__(valo1, valo2)
    def calcArea(self):
        return self.__valor1 * self.__valor2
        '''
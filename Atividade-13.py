class Creeper:
    def __init__(self, velocidade, raioDeExplosao, raioDePerseguicao, periodo, queimar):
        self.velocidade = velocidade
        self.raioDeExplosao = raioDeExplosao
        self.raioDePerseguicao = raioDePerseguicao
        self.periodo = periodo
        self.queimar = queimar
        
    def toString(self):
        return f"{self.velocidade} {self.raioDeExplosao} {self.raioDePerseguicao} {self.periodo} {self.queimar}"

class Esqueleto:
    def __init__(self, velocidade, raioDeVisao, danoDeflecha, periodo, queimar):
        self.velocidade = velocidade
        self.raioDeVisao = raioDeVisao
        self.danoDeFlecha = danoDeflecha
        self.periodo = periodo
        self.queimar = queimar
        
    def toString(self):
        return f"{self.velocidade} {self.raioDeVisao} {self.danoDeFlecha} {self.periodo} {self.queimar}"

creeper = Creeper(2, 20, 5, "manha e noite", False)
esqueleto = Esqueleto(5, 12, .05, "Noite", True)

print(creeper.toString())
print(esqueleto.toString())

#Unificaçao das duas classes
'''
class Mobi:
    def __init__(self,tipo, velocidade, danoDeAtaque, raioDePerseguicao, periodo, queimar, raioDeAtaque):
        self.tipo = tipo
        self.velocidade = velocidade
        self.danoDeAtaque = danoDeAtaque
        self.raioDePerseguicao = raioDePerseguicao
        self.periodo = periodo
        self.queimar = queimar
        self.raioDeAtaque = raioDeAtaque
        
    def toString(self):
        return f"{self.tipo} {self.velocidade} {self.danoDeAtaque} {self.raioDePerseguicao} {self.periodo} {self.queimar} {self.raioDeAtaque}"

creeper = Mobi("\ncreeper", 2,  20, 5, "manha e noite", False, 5)
esqueleto = Mobi("Esqueleto", 5, 12, .05, "Noite", True, 12)

print(creeper.toString())
print(esqueleto.toString())
'''
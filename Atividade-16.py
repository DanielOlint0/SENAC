class Pokemon:
    def __init__(self, hp, iv, tipo, nome, ataqueRapido, ataqueCarregado):
        self.__hp = hp
        self.__iv = iv
        self.__tipo = tipo
        self.__nome = nome
        self.__ataqueRapido = ataqueRapido
        self.__energiaAcumulada = 0
        self.__ataqueCarregado = ataqueCarregado

    def get_hp(self):
        return self.__hp
        
    def set_hp(self, valor):
        self.__hp = valor

    def get_iv(self):
        return self.__iv
        
    def set_iv(self, valor):
        self.__iv = valor

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, valor):
        self.__tipo = valor

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, valor):
        self.__nome = valor
    
    def get_ataqueRapido(self):
        return self.__ataqueRapido
    
    def set_ataqueRapido(self, valor):
        self.__ataqueRapido = valor

    def get_ataqueCarregado(self):
        return self.__ataqueCarregado
   
    def set_ataqueCarregado(self, valor):
        self.__ataqueCarregado = valor

    def get_energiaAcumulada(self):
        return self.__energiaAcumulada
        
    def set_energiaAcumulada(self, valor):
        self.__energiaAcumulada = valor
    def atacar(self):
        ataqueUsado = None
        if self.get_energiaAcumulada() >= self.get_ataqueCarregado().get_energiaAtivacao():
            print(f'Ataque carregado {self.get_ataqueCarregado().get_nome()} de {self.get_nome()} pronto!')
            dano = self.get_ataqueCarregado().get_dano() * self.get_iv()
            ataqueUsado = self.get_ataqueCarregado().get_nome()
            self.set_energiaAcumulada(self.get_energiaAcumulada() - self.get_ataqueCarregado().get_energiaAtivacao())
        else:
            dano = (self.get_ataqueRapido().get_dano() * self.get_iv()) / 65
            self.set_energiaAcumulada(self.get_energiaAcumulada() + self.get_ataqueRapido().get_geraEnergia())
            ataqueUsado = self.get_ataqueRapido().get_nome()
        return dano, ataqueUsado


    def __str__(self):
        return f"DADOS DO POKÉMON {self.__nome}:\nHP: {self.__hp}\nIV: {self.__iv}\nTipo: {self.__tipo}\nDADOS DO ATAQUE RÁPIDO\nNome: {self.__ataqueRapido}\nDADOS DO ATAQUE CARREGADO\nNome: {'Nome: '.join(map(str, self.__ataqueCarregado))}"

class Ataque:
    def __init__(self, nome, dano, tipo):
        self.__nome = nome
        self.__dano = dano
        self.__tipo = tipo

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, valor):
        self.__nome = valor

    def get_dano(self):
        return self.__dano
    
    def set_dano(self, valor):
        self.__dano = valor

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, valor):
        self.__tipo = valor

    def get_geraEnergia(self):
        return self.__geraEnergia
    
    def set_geraEnergia(self, valor):
        self.__geraEnergia = valor

    def __str__(self):
        return f'{self.__nome}\nDano: {self.__dano}\nTipo: {self.__tipo}\nEnergia gerada: {self.__geraEnergia}'

class AtaqueRapido(Ataque):
    def __init__(self, gerarEnergia, nome, dano, tipo):
        Ataque.__init__(self, nome, dano, tipo)
        self.__geraEnergia = gerarEnergia

    def get_geraEnergia(self):
        return self.__geraEnergia
    
    def set_geraEnergia(self, valor):
        self.__geraEnergia = valor

    def __str__(self):
        return f'{self.__nome}\nDano: {self.__dano}\nTipo: {self.__tipo}\nEnergia gerada: {self.__geraEnergia}'

class AtaqueCarregado(Ataque):
    def __init__(self, energiaAtivacao, nome, dano, tipo):
        Ataque.__init__(self, nome, dano, tipo)
        self.__energiaAtivacao = energiaAtivacao

    def get_energiaAtivacao(self):
        return self.__energiaAtivacao
    
    def set_energiaAtivacao(self, valor):
        self.__energiaAtivacao = valor

    def __str__(self):
        return f'{self.__nome}\nTipo: {self.__tipo}\nEnergia de ativação: {self.__energiaAtivacao}\nDano: {self.__dano}'

class BatalhaPokemon:
    def __init__(self, pokemonA, pokemonB):
        self.__pokemonA = pokemonA
        self.__pokemonB = pokemonB

    def get_pokemonA(self):
        return self.__pokemonA
    
    def set_pokemonA(self, valor):
        self.__pokemonA = valor

    def get_pokemonB(self):
        return self.__pokemonB
    
    def set_pokemonB(self, valor):
        self.__pokemonB = valor

    def batalha(self):
        
        print(F'___BATALHA POKÉMON___\n {self.__pokemonA.get_nome()} x {self.__pokemonB.get_nome()}')

        while self.get_pokemonA().get_hp() > 0 and self.get_pokemonB().get_hp() > 0:
            dano_pokemon_A, ataque_A = self.get_pokemonA().atacar() 

            self.get_pokemonB().set_hp(self.get_pokemonB().get_hp() - dano_pokemon_A)

            print(f"\n{self.get_pokemonA().get_nome()} atacou {self.get_pokemonB().get_nome()} com {ataque_A}")
            print(f'Dano causado {dano_pokemon_A:.2f}\n')
            print(f'HP de {self.get_pokemonA().get_nome()}: {self.get_pokemonA().get_hp():.2f}')
            print(f'Hp de {self.get_pokemonB().get_nome()} : {self.get_pokemonB().get_hp():.2f}')
            print('____________________________________________')

            if self.get_pokemonB().get_hp() <= 0:
                break

            dano_pokemon_B, ataque_B = self.get_pokemonB().atacar()
            self.get_pokemonA().set_hp(self.get_pokemonA().get_hp() - dano_pokemon_B)

            print(f'\n{self.get_pokemonB().get_nome()} atacou {self.get_pokemonA().get_nome()} com {ataque_B}')
            print(f'Dano causado {dano_pokemon_B:.2f}\n')
            print(f'HP de {self.get_pokemonA().get_nome()}: {self.get_pokemonA().get_hp():.2f}')
            print(f'Hp de {self.get_pokemonB().get_nome()} : {self.get_pokemonB().get_hp():.2f}')
            print('____________________________________________')

        if self.get_pokemonA().get_hp() <= 0:
            print(f"\n{self.get_pokemonA().get_nome().upper()} perdeu!")
            print(f"{self.get_pokemonB().get_nome().upper()} venceu a batalha!")

        else:
            print(f"\n{self.get_pokemonB().get_nome().upper()} perdeu!")
            print(f"{self.get_pokemonA().get_nome().upper()} venceu a batalha!")

cachoeira = AtaqueRapido(16, 'Cachoeira', 7, 'Água')
nevasca = AtaqueCarregado(65, 'Nevasca', 140, 'Gelo')
kyogre = Pokemon(174, 45, ['Água'], 'Kyogre', cachoeira, nevasca)

caudaDeDragao = AtaqueRapido(9, 'Cauda de dragão', 13, 'Dragão')
meteoro = AtaqueCarregado(65, 'Meteoro do Dragão', 150, 'Dragão')
garra = AtaqueCarregado(35, 'Garra do Dragão', 50, 'Dragão')
dragonite = Pokemon(177, 44, ['Dragão', 'Voador'], 'Dragonite', caudaDeDragao, garra)

batalha = BatalhaPokemon(dragonite, kyogre)
batalha.batalha()
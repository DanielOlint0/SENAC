class DispositivoEletronico:
    def produto(self):
        pass
    def acaoDoDispositivo(self):
        pass

class Impressora(DispositivoEletronico):
    def produto(self):
        return "Hp DeskJet"
    def acaoDoDispositivo(self):
        return "Esta imprimindo"

class AspiradorDePo(DispositivoEletronico):
    def produto(self):
        return "Fast Clean Plus"
    def acaoDoDispositivo(self):
        return "esta aspirando"
    
def eletronicos(dispositivos):
    for dispositivo in dispositivos:
        print(f'O dispositivo {dispositivo.produto()} esta {dispositivo.acaoDoDispositivo()}')

dispositivos = [Impressora(), AspiradorDePo()]
eletronicos(dispositivos)
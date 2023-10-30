from model.computador import Computador
from model.escritor import Escritor
from model.maquinaDeDatilografia import MaquinaDeDatilografia

escritor = Escritor("Machado de Assis")
computador = Computador("DELL")
maquinaDeDatilografia = MaquinaDeDatilografia(1988)

escritor.setInsturmentoDeTrabalho(computador)
escritor.getInsturmentoDeTrabalho().escrever()
escritor.setInsturmentoDeTrabalho(maquinaDeDatilografia)
escritor.getInsturmentoDeTrabalho().escrever()  
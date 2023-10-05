import random

tamLista = int(input("Tamanho da lista: "))

Lista = []

for numeroAleatorio in range(tamLista):
    Lista.append(random.randint(1, 10))

print(Lista)

def soma(Lista, tamanho):
    if tamanho == 0:
        return 0
    else:
        return Lista[tamanho-1] + soma(Lista, tamanho-1)

print("Resultado:", soma(Lista, tamLista))
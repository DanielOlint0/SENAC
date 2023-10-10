contador = int(6)
soma = int(0)

while(contador > 0):
    if(contador%2 == 0):
        soma += contador
    contador -= 1
print(soma)
del(contador, soma)
#organizando o github
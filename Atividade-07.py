contador = int(input())
Fatorial = int(1)

if(contador != 0 or contador != 1):
    while(contador >= 1):
        Fatorial *= contador
        contador -= 1
    print(Fatorial)
else: print("1")
del(contador, Fatorial)
#organizando o github
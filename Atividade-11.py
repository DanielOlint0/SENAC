def mmc(n1, n2, divi = 2, multi = 1):
    if n1 == 1 and n2 == 1:
        return multi
    if testePrimo(divi)==True:
        while n1 % divi == 0 or n2 % divi == 0:
            multi *= divi
            if n1 % divi == 0:
                n1 //= divi
            if n2 % divi ==0:
                n2 //= divi
    return mmc(n1, n2, divi+1, multi)

def testePrimo(n):
    aux = 0
    if n >= 2:
        for i in range(1, n):
            if n % i ==0:
                aux += 1
            if aux <= 1:
                return True
    return False

numero1 = int(input("Entre com um numero: "))
numero2 = int(input("Entre com um numero: "))

print("Resultado:", mmc(numero1,numero2))
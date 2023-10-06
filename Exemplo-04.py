a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

delta = b*b - 4 * a *c

del(c)
if(delta == 0):
    x = -b/(2*a)
    print(x)
    del(x)
elif(delta > 0):
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print(x1, x2)
    del(x1,x2)
else:
    print("x1 e x2 não possuem raizes reais")
    
del(a,b,delta)
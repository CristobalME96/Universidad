x = float(input("ingrese conejos"))
y = float(input("ingrese lobos"))

alpha = 3*10**(-3)
beta = 8*10**(-5)
gamma = 5*10**(-3)
delta = 6*10**(-6)

dias = 0
while x > 1:
    dias += 1
    dx = x*(alpha - beta*y)
    dy = -y*(gamma - delta *x)

    x =x + dx
    y =y + dy
    print("variacion de conejos: ", dx, " nuevo total: ", x)
    print("variacion de lobos: ", dy, " nuevo total: ", y)
print(dias)

hora = input("ingrese la hora: ")
H = int(hora[0:2])
M = int(hora[3:5])
S = int(hora[6:8])

for i in range(0, 60):
    S += 1
    if S == 60:
        S = 0
        M += 1
        if M == 60:
            M = 0
            H += 1
            if H == 24:
                H = 0
    print(str(H) + ":" + str(M) + ":" + str(S))

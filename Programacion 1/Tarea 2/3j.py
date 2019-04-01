print("Se calculara la cantidad de rebotes que da una pelota de tenis desde cierta altura")
alt = float(input("Ingese la altura:"))
i = 0
H_roce = alt
H_sin_roce = alt
while H_sin_roce > 0.03:
    if H_roce > 0.03:
        H_roce = (H_roce * 5/7) - ((H_roce * 5/7) * 0.06)
        if H_roce < 0.03:
            print("Si cae de", alt, "metros con roce, rebota", i, "veces")
    if H_sin_roce > 0.03:
        H_sin_roce = (H_sin_roce * 5/7)
        print(H_sin_roce)
        if H_sin_roce < 0.03:
            print("Si cae de", alt, "metros sin roce, rebota", i, "veces")
    i += 1

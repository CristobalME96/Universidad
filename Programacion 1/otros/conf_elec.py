L=["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "5f", "5d", "6p", "7s", "4f", "6d", "7p"]

tabla=["H", "He", "Li",	"Be", "B", "C",	"N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",	"Ca", "Sc",	"Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",	"Nb", "Mo",	"Tc", "Ru",	"Rh", "Pd",	"Ag", "Cd",	"In", "Sn",	"Sb", "Te",	"I", "X", "Cs",	"Ba", "La",	"Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",	"Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt",	"Au",	"Hg",	"TI", "Pb",	"Bi",	"Po",	"At",	"Rn", "Fr", "Ra", "Ac",	"Th", "Pa", "U", "Np", "Pu", "Am",	"Cm", "Bk", "Cf", "Es",	"Fm",	"Md", "No",	"Lr", "Rf",	"Db", "Sg",	"Bh",	"Hs", "Mt",	"Ds", "Rg",	"Cn", "Nh", "FI", "Mc",	"Lv",	"Ts", "Og"] # lista con los elementos

def n_atomico(elemento, tabla):
    for i in range (len(tabla)):
        if tabla[i] == elemento:
            Z=i+1
    return Z

def conf_electronica(z, L):
    conf = L[0]
    var = 0
    pos = 0
    while z > 0:
        z -=1
        var += 1
        if conf[len(conf)-1] == 's' and var == 2:
            conf += str(var)
            var = 0
            pos += 1
            conf += " " + L[pos]
        elif conf[len(conf)-1] == 'p' and var == 6:
            conf += str(var)
            var = 0
            pos += 1
            conf += " " + L[pos]
        elif conf[len(conf)-1] == 'd' and var == 10:
            conf += str(var)
            var = 0
            pos += 1
            conf += " " + L[pos]
        elif conf[len(conf)-1] == 'f' and var == 14:
            conf += str(var)
            var = 0
            pos += 1
            conf += " " + L[pos]
        elif z == 0:
            conf += str(var)
    return conf

elemento=str(input("ingrese un elemento: "))
z = n_atomico(elemento, tabla)
print(conf_electronica(z, L))

# hold 4
# kasperP, kristoffer, laurits


def KegleV(V, r, h):
    resultat = 0
    if V == 0:
        V = (3,14/3)*r*r*h
        resultat = V
    elif r == 0:
        r = math.sqrt(V/((3,14/3)*h))
        resultat = r
    elif h == 0:
        h = V/((3,14/3)*r*r)
        resultat = h
    return resultat

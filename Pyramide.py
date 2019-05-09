# hold 9
# thomas, victor kristoffer




def PyramideV(V, G, h):
    resultat = 0
    if V == 0:
        V = (1/3)*G*h
        resultat = V

    if G == 0:
        G = V/((1/3)*h)
        resultat = G

    if h == 0:
        h = V/((1/3)*G)
        resultat = h

    return resultat
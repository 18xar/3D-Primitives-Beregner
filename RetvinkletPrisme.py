# hold 11
# William og Wilfred


def RetvinkletPrisme(V, G, h):
    resultat = 0

    if V==0:
        V=G*h
        resultat=V

    if G==0:
        G = V/H
        resultat=G
    if h==0:
        h=V/G
        resultat=h

    return resultat


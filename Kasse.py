# hold 3
# emma, isabella, kacper
import math

def KasseV(V, l, b, h):

    if (V == 0):
        V = l * b * h

        resultat = V

    if (l == 0):
        l = V / (b * h)

        resultat = l

    if (b == 0):
        b = V / (l * h)

        resultat = b

    if (h == 0):
        h = V / (b * l)

        resultat = h

    return resultat


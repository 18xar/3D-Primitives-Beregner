# hold 3
# emma, isabella, kacper
import math

def KasseV(V, l, b, h):

    if (V == 0):
        V = l * b * h

    if (l == 0):
        l = V / (b * h)

    if (b == 0):
        b = V / (l * h)

    if (h == 0):
        h = V / (b * l)

    resultat = V, l, b, h
    return resultat


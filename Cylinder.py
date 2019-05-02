# hold 1
# andreas, asger, aslak
import math


def CylinderV(V, r, h):
    resultat = 0
    if V == 0:
        V = math.pi * r**2 * h
        resultat = V
    if r == 0:
        r = math.sqrt(V / (math.pi * h))
        resultat = r
    if h == 0:
        h = V / (math.pi * r**2)
        resultat = h
    return resultat
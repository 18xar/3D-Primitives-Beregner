# hold 6
# Mohammad, Nichi, Nani?!?!
import math

def KugleV(V, r):
    resultat = 0
    if V == 0:
        resultat = 4/3 * math.pi * math.pow(r, 3)
    if r == 0:
        resultat = math.pow((3*V)/(4*math.pi), 1/3)
    return resultat
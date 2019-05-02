import math


def KugleUdsnitV(V, r, h):
    resultat = 0

    if(V == 0):
        V = (math.pi/6) * 4*r**2 * h
        resultat = V

    if(r == 0):
        r = math.sqrt(V/((math.pi/6)*h*4))
        resultat = r

    if(h == 0):
        h = V/((math.pi/6) * 4*r**2)
        resultat = h

    return resultat

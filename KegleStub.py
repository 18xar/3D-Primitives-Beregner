# hold 5
# luccas, martin, matias
import math

def KegleStubV(V, R, r, h):
    resultat = 0
    #V = pi/3 * h * (R^2 + r^2 + R * r)

    if V == 0:
        resultat = math.pi / 3 * h * (R ^ 2 + r ^ 2 + R * r)

    elif R == 0:
        a = (math.pi/3) * h
        b = (math.pi/3) * h * r
        c = (math.pi/3) * h * (r*r) - V
        R1 = (-1*b + math.sqrt(((b*b) - 4 * a * c)))/(2 * a)
        R2 = (-1*b - math.sqrt(((b*b) - 4 * a * c)))/(2 * a)

        resultat =

    elif h == 0:
        resultat = V/(math.pi/3)*(R*R + r*r + R * r)

    return resultat

#R^2 + R * r

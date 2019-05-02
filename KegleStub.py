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

        if R1 > 0:
            resultat = R1
        elif R2 > 0:
            resultat = R2


    elif r == 0:
        a = (math.pi/3) * h
        b = (math.pi/3) * h * R
        c = ((math.pi/3) * h * R*R) - V
        r1 = (-1 * b + math.sqrt(((b * b) - 4 * a * c))) / (2 * a)
        r2 = (-1 * b - math.sqrt(((b * b) - 4 * a * c))) / (2 * a)

        if r1 > 0:
            resultat = r1
        elif r2 > 0:
            resultat = r2


    elif h == 0:
        resultat = V/(math.pi/3)*(R*R + r*r + R * r)

    return resultat

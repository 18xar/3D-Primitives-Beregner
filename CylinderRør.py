# hold 2
# buster, christian, daniel

def CylinderRørV(V, R, r, h):
    resultat = 0

    import math

    if(R == 0):

        R = math.sqrt((V+h*3,14159265*r*r)/(h*3,14159265))

        resultat = R

    if(r == 0):

        r = math.sqrt((V-3,14159265*R*R*h)/(3,14159265*h))

        resultat = r

    if(h == 0):

        h = V/(3,14159265*R*R-3,14159265*r*r)

        resultat = h

    if(V == 0):

        V = h*3,14159265*R*R-h*3,14159265*r*r

        resultat = V

    return resultat
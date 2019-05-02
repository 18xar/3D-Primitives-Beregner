# hold 7
# oliver, oscar, ,otto
import math

def KugleAfsnitV(V, a, h):

    if V==0:
        V=(math.pi/6)*h*(3*a*a+h*h)
        resultat=V
    elif a == 0:
        a=math.sqrt((V/(math.pi / 6) * h)/(3*h*h))
        resultat=a

    elif h == 0:
        h=math.sqrt((V/(math.pi / 6) * a)/(3*a*a))
        resultat=h

    return resultat


# def addition(a,b):
#     return a+b
#
# def ma_fonction(x,y,f,**params):
#     print(x,y,f(params))
#
# ma_fonction(x=1, y=2, f=addition, a=1, b=2)
import math

def calcul_masse_volume_ellipsoide (a=1,b=2,c=3,masse_volumique=4):
    volume = a*b*c*(4/3)*math.pi
    masse = volume * masse_volumique
    return volume,masse
v,m = calcul_masse_volume_ellipsoide(masse_volumique=10)
print(v,m)
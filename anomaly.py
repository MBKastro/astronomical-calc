import math
from math import sin, cos, tan, atan


#
# function anomaly. input mean anomaly, eccentricity (s)
# calculates two global vars  ea eccentric anomaly, nu : true anomaly
#
def anomaly(w, s):
    print("Solving Kepler's equation")
    global nu, ea
    tpi = 6.283185308
    m = w - tpi * int(w / tpi)
    ea = m
    dla = ea - (s * sin(ea)) - m
    while (abs(dla) >= 1E-6):
        dla = dla / (1 - (s * math.cos(ea)))
        ea = ea - dla
        dla = ea - (s * sin(ea)) - m
    tnu2 = math.sqrt((1 + s) / (1 - s)) * tan(ea / 2)
    nu = 2 * math.atan(tnu2)
    return


#
# convert rad/deg
#
def fnrad(w):
    return (1.745329252E-2 * w)


#
def fndeg(w):
    return (5.729577951E1 * w)


#
# Handling anomaly
#
ma = 43.7172
s = 0.965
nuu = 0
eaa = 0
ma = fnrad(ma)
anomaly(ma, s)
nu = fndeg(nu)
ea = fndeg(ea)
print('True anomaly      ', nu)
print('Eccentric anomaly ', ea)

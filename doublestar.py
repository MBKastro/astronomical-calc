#
# doublestar
#
# read WDS
#
f = open('6thorbiths.txt', 'r')
# WDS #
wds = []
# Discoverer
dis = []
# Period in P_u
Per = []
# Period units
P_u = []
# Semimajor axis, alfa in alfa_u
alfa = []
# Semimajor axis units
alfa_u = []
# Inclination
incl = []
# Ascending node in degrees
Omega = []
# Time of periastron (no unit..)
time = []
# Eccentricity
ecc = []
# Longitude of periastron in degrees
omega = []
#
for contents in f:
    wds.append(contents[19:29])
    dis.append(contents[30:42])
#
    if (contents[81:90]) > '    .    ':
        Per.append(float(contents[81:90]))
    else:
        Per.append(0)
#
    P_u.append(contents[92:93])
#
    if contents[104:114] > '    .     ':
        alfa.append(float(contents[104:114]))
    else:
        alfa.append(0)
#
    alfa_u.append(contents[114:115])
#
    if contents[125:133] > '   .    ':
        incl.append(float(contents[125:133]))
    else:
        incl.append(0)
#   Node (Omega), in degrees
    if contents[143:151] > '   .    ':
        Omega.append(float(contents[143:151]))
    else:
        Omega.append(0)
#
    if contents[162:174] > '     .      ':
        time.append(float(contents[162:174]))
    else:
        time.append(0)
#
    if contents[187:195] > ' .      ':
        ecc.append(float(contents[187:195]))
    else:
        ecc.append(0)
#   Longitude of periastron (omega), in degrees
    if contents[205:213] > '   .    ':
        omega.append(float(contents[205:213]))
    else:
        omega.append(0)
f.close()
#
# input date and Keplerian elements
# output position angle in degrees and separation in arc secs for date of obs.
# repeats calculations by incrementing date of obs.
#
#
from math import sin, cos, tan, atan, sqrt


#
def fnrad(w):
    return (1.745329252E-2 * w)


#
# Per[x], time[x], alfa[x], ecc[x], incl[x], omega[x], Omega[x]
#
def doublestar(p, t, a1, s, i, w, l, d):
    global pa, sep
    px = 3.141592654
    c = 6.283185307
    i = fnrad(i)
    l = fnrad(l)
    w = fnrad(w)
    n = c / p
    #
    ma = n * (d - t)
    #
    m = round(ma - c * int(ma / c),7)
    ea = m
    a = round(ea - (s * sin(ea)) - m,7)
    while abs(a) >= 1E-6:
        a = a / round((1 - (s * cos(ea))),7)
        ea = round(ea - a,7)
        a = round(ea - (s * sin(ea)) - m,7)
    #
    tu = sqrt((1 + s) / (1 - s)) * tan(ea / 2)
    nu = 2 * atan(tu)
    #
    print(a1)
    print(s)
    print(cos(ea))
    print(w)
    print(i)
    #
    r = a1 - a1 * s * cos(ea)
    y = sin(nu + w) * cos(i)
    x = cos(nu + w)
    q = atan(y / x)
    #
    print("efter")
    #
    print(r)
    print(y)
    print(x)
    print(q)
    #
    if x < 0:
        q = q + px
    else:
        if q < 0:
           q = q + c
    #
    print(q)
    #
    th = q + l
    if th > c:
        th = th - c
    rh = r * x / cos(q)
    #
    pa = int(th / fnrad(1) * 10 + 0.5) / 10
    sep = int(rh * 100 + 0.5) / 100
    print('year = ', d)
    print('pa   = ', pa, ' deg')
    print('sep. = ', sep, ' arcsec')
    line = str(d) + ';' + str(sep) + ';' + str(pa)
    f.write(line)
    f.write('\n')
    return ()


#
# input vars
#
i_wds = input('WDS ')
x = wds.index(i_wds)
print(dis[x], Per[x], time[x], alfa[x], ecc[x], incl[x], omega[x], Omega[x])
d = float(input('date of obs. (year)              '))
f = open(i_wds+' position.txt', 'w')
line = 'year;sep;pa'
f.write(line)
f.write('\n')
doublestar(Per[x], time[x], alfa[x], ecc[x], incl[x], omega[x], Omega[x], d)
#
# convert angle to a negative y-axis corresponding to 0 deg North by substracting 90 and adding 360 if result is < 0
# x_co = distance * cos(angle) + x0 (another position than 0,0)
# y_co = distance * sin(angle) + y0
# print (sep * cos (pa))
# print (sep * sin (pa))
#
print(' ')
#
# check for more calculations? input increment.
#
inc_p = float(input('increment,inc_p (years)           '))
num_i = int(input('no of increments, num_i           '))
# example
if inc_p > 0 and num_i > 0:  # 10, 1
    dd = d + inc_p  # 2033 = 2023 + 10
    while dd <= d + (num_i * inc_p):  # while 2033 <= 2023 + 1 * 10 (yes)
        doublestar(Per[x], time[x], alfa[x], ecc[x], incl[x], omega[x], Omega[x], d)  # new calc.
        dd = dd + inc_p  # 2043 = 2033 + 10 (end while)
#

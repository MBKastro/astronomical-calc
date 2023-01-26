# doublestar
# input date and Keplerian elements
# output position angle in degrees and separation in arc secs for date of obs.
# repeats calculations by incrementing date of obs.
#
# read WDS
f = open('6thorbiths.txt', 'r')
# WDS #
wds = []
# Discoverer designation
dis = []
# Period in units
Per = []
# Period units
P_u = []
# Semimajor axis, alfa in units
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
# WDS
for contents in f:
    wds.append(contents[0:18])
    dis.append(contents[30:42])
    #
    # Period in units
    if (contents[81:90]) > '    .    ':
        Per.append(float(contents[81:90]))
    else:
        Per.append(0)
    #
    # Period units
    P_u.append(contents[92:93])
    #
    # Semimajor axis, alfa in units
    if contents[104:114] > '    .     ':
        alfa.append(float(contents[104:114]))
    else:
        alfa.append(0)
    #
    # Semimajor axis units
    alfa_u.append(contents[114:115])
    #
    # Inclination
    if contents[125:133] > '   .    ':
        incl.append(float(contents[125:133]))
    else:
        incl.append(0)
    #
    # Node (Omega), in degrees
    if contents[143:151] > '   .    ':
        Omega.append(float(contents[143:151]))
    else:
        Omega.append(0)
    #
    # Time of periastron (no unit..)
    if contents[162:174] > '     .      ':
        time.append(float(contents[162:174]))
    else:
        time.append(0)
    #
    # Eccentricity
    if contents[187:195] > ' .      ':
        ecc.append(float(contents[187:195]))
    else:
        ecc.append(0)
    #
    # Longitude of periastron (omega), in degrees
    if contents[205:213] > '   .    ':
        omega.append(float(contents[205:213]))
    else:
        omega.append(0)
f.close()
#
from math import sin, cos, tan, atan, sqrt
#
def fnrad(w):
    return (1.745329252E-2 * w)
#
# Per[x], time[x], alfa[x], ecc[x], incl[x], omega[x], Omega[x], obs.date
def doublestar(p, t, a1, s, i, w, l, d):
    global pa, sep, x_co, y_co
    px = 3.141592654
    c = 6.283185307
    i = fnrad(i)
    l = fnrad(l)
    w = fnrad(w)
    n = c / p
    ma = n * (d - t)
    m = ma - c * int(ma / c)
    ea = m
    a = ea - (s * sin(ea)) - m
    while abs(a) >= 1E-15:
        a = a / (1 - (s * cos(ea)))
        ea = ea - a
        a = ea - (s * sin(ea)) - m
    #
    tu = sqrt((1 + s) / (1 - s)) * tan(ea / 2)
    nu = 2 * atan(tu)
    r = a1 - a1 * s * cos(ea)
    y = sin(nu + w) * cos(i)
    x = cos(nu + w)
    q = atan(y / x)
    #
    if x < 0:
        q = q + px
    else:
        if q < 0:
            q = q + c
    #
    th = q + l
    if th > c:
        th = th - c
    rh = r * x / cos(q)
    pa = int(th / fnrad(1) * 10 + 0.5) / 10
    sep = int(rh * 100 + 0.5) / 100
    #
#    print('year = ', d)
#    print('pa   = ', pa, ' deg')
#    print('sep. = ', sep, ' arcsec')
    #
    # Convert polar to x,y coordinates; flopping x with y and (-)y to invert so 0 degrees is down on y-axis
    # x_co = distance * cos(radians (angle)) sep * sin(radians(pa))
    # y_co = distance * sin(radians (angle)) (-)sep * cos(radians(pa))
    x_co = round(sep * sin(fnrad(pa)), 2)
    y_co = round(sep * -1 * cos(fnrad(pa)), 2)
    #
    line = str(d) + ';' + str(sep) + ';' + str(pa) + ';' + str(x_co) + ';' + str(y_co)
    f.write(line)
    f.write('\n')
    return ()
#
# input vars. Find WDS.
#
i_wds = input('WDS ')
ix = wds.index(i_wds)
print('Disc         Period Time alfa Ecc Inc omega Omega')
print(dis[ix], Per[ix], time[ix], alfa[ix], ecc[ix], incl[ix], omega[ix], Omega[ix])
d = float(input('date of obs. (year)              '))
f = open(i_wds + ' position.txt', 'w')
line = 'year;sep;pa'
f.write(line)
f.write('\n')
doublestar(Per[ix], time[ix], alfa[ix], ecc[ix], incl[ix], omega[ix], Omega[ix], d)
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
        doublestar(Per[ix], time[ix], alfa[ix], ecc[ix], incl[ix], omega[ix], Omega[ix], dd)  # new calc.
        dd = dd + inc_p  # 2043 = 2033 + 10 (end while)
#
import numpy as np
import matplotlib.pyplot as plt
import csv

x_co = []
y_co = []
f = open(i_wds + ' position.txt', 'r')
for rec in f:
    rec = csv.reader(f, delimiter=";")
    for row in rec:
        x = float(row[3])
        y = float(row[4])
        x_co.append(x)
        y_co.append(y)
colors = (0, 0, 0)
area = np.pi * 3
plt.scatter(x_co, y_co, s=area, alpha=0.5, color='b')
plt.scatter(0, 0, s=area, alpha=0.5, color='r')
# plt.scatter(1, 1, s=area, alpha=0.5, color='g')
plt.title('WDS ' + i_wds)
plt.xlabel('x')
plt.ylabel('y')
plt.axvline(0, 0, 1, color='r')
plt.axhline(0, 0, 1, color='r')
plt.show()

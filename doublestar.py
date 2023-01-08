#
# function doublestar
#
# input date and Keplerian elements
# calculates position angle in degrees and separation in arcsec for date of obs.
# and repeats calculations by incrementing date of obs. in years
#
from math import sin, cos, tan, atan, sqrt


#
def fnrad(w):
    return (1.745329252E-2 * w)


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
    m = ma - c * int(ma / c)
    ea = m
    a = ea - (s * sin(ea)) - m
    while abs(a) >= 1E-6:
        a = a / (1 - (s * cos(ea)))
        ea = ea - a
        a = ea - (s * sin(ea)) - m
    #
    tu = sqrt((1 + s) / (1 - s)) * tan(ea / 2)
    nu = 2 * atan(tu)
    #
    r = a1 - a1 * s * cos(ea)
    y = sin(nu + w) * cos(i)
    x = cos(nu + w)
    q = atan(y / x)
    #
    if x >= 0 and q < 0:
        q = q + c
    else:
        q = q + px
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
p = float(input('period, p (years)                '))
t = float(input('date of periastron, t            '))
a1 = float(input('semi-major axis, a               '))
s = float(input('eccentricity,e                   '))
i = float(input('incliniation,i                   '))
w = float(input('arg. of periastron, w            '))
l = float(input('pa of ascending node             '))
d = float(input('date of obs. (year)              '))
#
f = open('position.txt', 'w')
line = 'year;sep;pa'
f.write(line)
f.write('\n')
#
doublestar(p, t, a1, s, i, w, l, d)
print(' ')
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
        doublestar(p, t, a1, s, i, w, l, dd)  # new calc.
        dd = dd + inc_p  # 2043 = 2033 + 10 (end while)
#

import math
from math import sin, cos, tan, atan, sqrt


def fnrad(w):
    return (1.745329252E-2 * w)


def fndeg(w):
    return (5.729577951E1 * w)


def fnasn(w):
    return (math.atan(w / (math.sqrt(1 - w * w) + 1E-20)))


#
#    function obliq
#
def obliq(dy, mn, yr):
    print('Obliq')
    t = julday(dy, mn, yr) / 36525
    print('t ', t)
    co = (((-1.81E-3 * t) + 5.9E-3) * t + 4.6845E1) * t
    eps = 2.345229444E1 - (co / 3600)
    # epsr is eps in radians
    # epsr=eps*1.745329252E-2
    print('eps ', eps)
    # print ('epsr ',eps)
    return (eps)


# return(epsr)
#
#    function julday
#
def itg(w):
    print('itg')
    print(w)
    print(abs(w))
    sgn = 1
    if w < 0:
        sgn = -1
    print(sgn * int(abs(w)))
    return (sgn * int(abs(w)))


#
def julday(dy, mn, yr):
    print('julday')
    mn1 = mn
    yr1 = yr
    b = 0
    if yr1 < 0:
        yr1 = yr1 + 1
    if mn < 3:
        mn1 = mn + 12
        yr1 = yr1 - 1
    if yr > 1582 or (yr == 1582 and mn == 10 and dy >= 15):
        a = int(yr1 / 100)
        b = 2 - a + int(a / 4)
    if yr1 >= 0:
        c = int(365.25 * yr1) - 694025
    else:
        c = itg((365.25 * yr1) - 0.75) - 694025
    d = int(30.6001 * (mn1 + 1))
    print('djd ', b + c + d + dy - 0.5)
    return (b + c + d + dy - 0.5)


#
# subroutine eqecl
# returns global vars px,qy
#
def eqecl(dy, mn, yr, x, y, sw):
    print('Eqecl')
    global px, qy
    pi = 3.1415926535
    tpi = 2 * pi
    # nutation: function nutat returns deps, here set to 0
    deps = 0
    eps = obliq(dy, mn, yr)
    eps1 = fnrad(eps + deps)
    seps = math.sin(eps1)
    ceps = math.cos(eps1)
    cy = math.cos(y)
    sy = math.sin(y)
    if abs(cy) < 1E-20:
        cy = 1E-20
    ty = sy / cy
    cx = math.cos(x)
    sx = math.sin(x)
    sq = (sy * ceps) - (cy * seps * sx * sw)
    q = fnasn(sq)
    a = (sx * ceps) + (ty * seps * sw)
    p = math.atan(a / cx)
    if cx < 0:
        p = p + pi
    if p > tpi:
        p = p - tpi
    if p < 0:
        p = p + tpi
    px = p
    qy = q
    return ()


#
# handling eqecl
#
print('Handling eqecl eq<->ecl')
dy = 28
mn = 5
yr = 2004
#
x = fnrad(277.00174456364283)
y = fnrad(-66.4054960573709)
sw = -1
#
# sw= 1 : convert RA/DEC to Ecl.Long/Lat. x=fnrad(RA*15)
# sw=-1 : convert Ecl.Long/Lat. to RA/DEC -
#
eqecl(dy, mn, yr, x, y, sw)
print(fndeg(px), fndeg(qy))

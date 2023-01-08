import math
from math import sin, tan


#
def fnrad(w):
    return 1.745329252E-2 * w


def fndeg(w):
    return (5.729577951E1 * w)


#
#    function julday
#
def itg(w):
    print('itg')
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
    return (b + c + d + dy - 0.5)


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
    print('ea ', ea)
    print('nu ', nu)
    return


#
# subroutine sun.
# input date & time: dy(+xd,xm,xs),mn,yr
#
def sun(dy, mn, yr):
    print('sun ', dy, mn, yr)
    global lsn, rsn
    #   call julday
    t = julday(dy, mn, yr) / 36525
    t2 = t * t
    a = 1.000021359E2 * t
    b = 360 * (a - int(a))
    ls = 2.7969668E2 + 3.025E-4 * t2 + b
    a = 9.999736042E1 * t
    b = 360 * (a - int(a))
    ms = 3.5847583E2 - (1.5E-4 + 3.3E-6 * t) * t2 + b
    s = 1.675104E-2 - 4.18E-5 * t - 1.26E-7 * t2
    ma = fnrad(ms)
    #   call anomaly for ea
    anomaly(ma, s)
    a = 6.255209472e1 * t
    b = 360 * (a - int(a))
    a1 = fnrad(153.23 + b)
    a = 1.251041894E2 * t
    b = 360 * (a - int(a))
    b1 = fnrad(216.57 + b)
    a = 9.156766028E1 * t
    b = 360 * (a - int(a))
    c1 = fnrad(312.69 + b)
    a = 1.236853095E3 * t
    b = 360 * (a - int(a))
    d1 = fnrad(350.74 - 1.44E-3 * t2 + b)
    e1 = fnrad(231.19 + 20.2 * t)
    a = 1.831353208E2 * t
    b = 360 * (a - int(a))
    h1 = fnrad(353.4 + b)
    dl = 1.34E-3 * math.cos(a1) + 1.54E-3 * math.cos(b1) \
         + 2E-3 * math.cos(c1) + 1.79E-3 * math.sin(d1) \
         + 1.78E-3 * math.sin(e1)
    dr = 5.43E-6 * math.sin(a1) + 1.575E-5 * math.sin(b1) \
         + 1.627E-5 * math.sin(c1) + 3.076E-5 * math.cos(d1) \
         + 9.27E-6 * math.sin(h1)
    lsn = nu + fnrad(ls - ms + dl)
    tpi = 6.283185308
    rsn = 1.0000002 * (1 - s * math.cos(ea)) + dr
    while (lsn < 0):
        lsn = lsn + tpi
    while (lsn > tpi):
        lsn = lsn - tpi
    return ()


#
# handle sun
#
print('Handling sun')
dy = 24.56587789
mn = 8
yr = -1984
#
sun(dy, mn, yr)
#
print('lsn deg.', fndeg(lsn))
print('rsn (AU) ', rsn)

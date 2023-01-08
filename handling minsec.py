#
# function minsec_dec
#
def minsec_dec(xd, xm, xs):
    sn = 1
    if xd < 0 or xm < 0 or xs < 0:
        sn = -1
    xd1 = abs(xd)
    xm1 = abs(xm)
    xs1 = abs(xs)
    return (((((xs1 / 60) + xm1) / 60) + xd1) * sn)


#
# function minsec_hms
#
def minsec_hms(x):
    xp = abs(x)
    xd = int(xp)
    a = (xp - xd) * 60
    xm = int(a)
    xs = int((a - xm) * 600 + 0.5) / 10
    s = " "
    if x < 0:
        s = "-"
    return (str(s) + str(xd) + " " + str(xm) + " " + str(xs))


#
# Handling program for MINSEC
print('Handling program for MINSEC')
print('Degrees/hours conversion')
#
#
x = minsec_dec(0, 0, 5.5)
print(x)
#
x = minsec_dec(-87, 12, 12)
print(x)
#
xd = minsec_hms(200.09351240395137)
print(xd)
#
xd = minsec_hms(0.0229165749243164)
print(xd)

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

import math
from math import sin, cos, tan, atan, sqrt


#
#
# function nutat
#
def nutat(dy,mn,yr):
    global dpsi,deps
    t=julday(dy,mn,yr)/36525
    t2=t*t
    a=1.000021358e2*t
    b=360*(a-int(a))
    ls=2.796967e2+3.03E-4*t2+b
    a=1.336855231e3*t
    b=360*(a-int(a))
    ld=2.704342e2-1.133E-3*t2+b
    a=9.999736056e1*t
    b=360*(a-int(a))
    ms=3.584758e2-1.5E-4*t2+b
    a=1.325552359e3*t
    b=360*(a-int(a))
    md=2.961046e2+9.192E-3*t2+b
    a=5.372616667*t
    b=360*(a-int(a))
    nm=2.591833e2+2.078E-3*t2-b
    tls=2*fnrad(ls)
    nm=fnrad(nm)
    tnm=2*fnrad(nm)
    ms=fnrad(ms)
    tld=2*fnrad(ld)
    md=fnrad(md)
    dpsi=(-17.2327-1.737E-2*t)*math.sin(nm)\
     +(-1.2729-1.3E-4*t)*math.sin(tls)\
     +2.088E-1*math.sin(tnm)-2.037E-1*math.sin(tld)\
     +(1.261E-1-3.1E-4*t)*math.sin(ms)\
     +6.75E-2*math.sin(md)\
     -(4.97E-2-1.2E-4*t)*math.sin(tls+ms)\
     -3.42E-2*math.sin(tld-nm)-2.61E-2*math.sin(tld+md)\
     +2.14E-2*math.sin(tls-ms)\
     -1.49E-2*math.sin(tls-tld+md)\
     +1.24E-2*math.sin(tls-nm)+1.14E-2*math.sin(tld-md)
    deps=(9.21+9.1E-4*t)*math.cos(nm)\
     +(5.522E-1-2.9E-4*t)*math.cos(tls)\
     -9.04E-2*math.cos(tnm)+8.84E-2*math.cos(tld)\
     +2.16E-2*math.cos(tls+ms)+1.83E-2*math.cos(tld-nm)\
     +1.13E-2*math.cos(tld+md)-9.3E-3*math.cos(tls-ms)\
     -6.6E-3*math.cos(tls-nm)
    dpsi=dpsi/3600
    deps=deps/3600
    return ()
#
#
# function minsec_hms
#
def minsec_hms(x):
 xp=abs(x)
 xd=int(xp)
 a=(xp-xd)*60
 xm=int(a)
 xs=int((a-xm)*600+0.5)/10
 s=" "
 if x<0:
   s="-"
 return(str(s)+str(xd)+" "+str(xm)+" "+str(xs))
#
def fnrad(w):
    return 1.745329252E-2*w
#
def itg(w):
   print ('itg')
   print (w)
   print (abs(w))
   sgn=1
   if w<0:
      sgn=-1
   print (sgn*int(abs(w)))
   return (sgn*int(abs(w)))
#
#
def julday(dy,mn,yr):
   print ('julday')
   mn1=mn
   yr1=yr
   b=0
   if yr1<0:
      yr1=yr1+1
   if mn<3:
      mn1=mn+12
      yr1=yr1-1
   if yr>1582 or (yr==1582 and mn==10 and dy>=15):
      a=int(yr1/100)
      b=2-a+int(a/4)
   if yr1>=0:
      c=int(365.25*yr1)-694025
   else:
      c=itg((365.25*yr1)-0.75)-694025
   d=int(30.6001*(mn1+1))
   print ('djd ', b+c+d+dy-0.5)
   return (b+c+d+dy-0.5)
#
#
dy=1.5
mn=1
yr=2000
nutat(dy, mn, yr)
dpsi=minsec_hms(dpsi)
deps=minsec_hms(deps)
print (dpsi, deps)
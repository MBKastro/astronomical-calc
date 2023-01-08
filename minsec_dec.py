#
# function minsec_dec
#
def minsec_dec(xd,xm,xs):
  sn=1
  if xd<0 or xm<0 or xs<0:
      sn=-1
  xd1=abs(xd)
  xm1=abs(xm)
  xs1=abs(xs)
  return(((((xs1/60)+xm1)/60)+xd1)*sn)
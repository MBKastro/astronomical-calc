#
#    function obliq
#
def obliq(dy, mn, yr):
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

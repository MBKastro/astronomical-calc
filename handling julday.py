#
#   handling  julday
#
print ('Calendar date to julian days')
dy=input('Calendar day ')
mn=input('         month ')
yr=input('         year ')
# int returns (integer) value of string
djd=julday(float(dy), int(mn), int(yr))
jd=djd+2415020
print('j days since 1900 jan 0.5: ',djd)
print('julian date ',jd)
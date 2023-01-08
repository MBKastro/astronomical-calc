#
#   handling  obliq
#
print('Handling obliquity of the ecliptic')
dy = input('Day   ')
mn = input('Month ')
yr = input('Year  ')
x = obliq(float(dy), int(mn), int(yr))
o = minsec_hms(x)
print('The mean obliquity is (Deg,Min,Sec) ', o)

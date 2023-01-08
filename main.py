f = open('6thorbiths.txt', 'r')
x = 1
for contents in f:
    wds = contents[19:30]
    dis = contents[30:42]
    if (contents[81:90]) > '    .    ':
        Per = float(contents[81:90])
    else:
        Per = 0
    P_u = contents[92:93]
    if contents[104:114] > '    .     ':
        alfa = float(contents[104:114])
    else:
        alfa = 0
    alfa_u = contents[114:115]
    if contents[125:133] > '   .    ':
        incl = float(contents[125:133])
    else:
        incl = 0
    if contents[143:151] > '   .    ':
        Omega = float(contents[143:151])
    else:
        Omega = 0
    if contents[162:164] > '  ':
        time = float(contents[162:164])
    else:
        time = 0
    if contents[205:213] > '   .    ':
        omega = float(contents[205:213])
    else:
        omega = 0
    print(x, wds, dis, Per, alfa, incl, Omega, time, omega)
    if dis == 'STF1424AB   ':
        print ('juhu')
    x = x + 1
f.close()

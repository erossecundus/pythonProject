lmin = int(input('entre lmin: '))
lmax = int(input('entre lmax: '))
d = int(input('entre d: '))

while lmin <= lmax:
    if lmin % d == 0:
        print(lmin)
    lmin += 1
print('fim')

S = input()
w = 0
e = 0

for s in S:
    if s=='W':
        w += 1
    elif s=='E':
        e += 1

if e>w:
    print('East')
else:
    print('West')
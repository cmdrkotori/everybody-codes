#!/usr/bin/python3
from itertools import batched
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

with open(notes(2025,13,1)) as f:
    z = list(map(int,f.read().strip().split('\n')))
y=[0]*(len(z)+1)
y[0] = 1
i = 0
for a,b in batched(z,2):
    y[1+i] = a
    y[-1-i] = b
    i += 1
print(y[2025%len(y)])

with open(notes(2025,13,2)) as f:
    z = [list(map(int,x.split('-'))) for x in f.read().strip().split('\n')]
def p2(z,num):
    y1 = [1]
    y2 = []
    for a,b in batched(z,2):
        a1,a2 = a
        b1,b2 = b
        for x in range(a1,a2+1):
            y1.append(x)
        for x in range(b1,b2+1):
            y2.append(x)
    y = y1
    y2.reverse();
    y.extend(y2)
    print(y[num%len(y)])
p2(z,20252025)

with open(notes(2025,13,3)) as f:
    z = [list(map(int,x.split('-'))) for x in f.read().strip().split('\n')]
p2(z,202520252025)

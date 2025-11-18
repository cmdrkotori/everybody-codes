#!/usr/bin/pypy3
from itertools import pairwise
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def simulate(p1):
    moved = True
    rnd = 0
    while moved:
        moved = False
        for i,j in pairwise(range(len(z))):
            if z[j] < z[i]:
                z[i] -= 1
                z[j] += 1
                moved = True
        if moved:
            rnd += 1
            if p1:
                print(f'{rnd} {" ".join(str(zz) for zz in z)} {sum([(i+1)*j for i,j in enumerate(z)])}')
    if p1:
        print('Commencing phase 2')
    moved = True
    while moved:
        moved = False
        for i,j in pairwise(range(len(z))):
            if z[j] > z[i]:
                z[j] -= 1
                z[i] += 1
                moved = True
        if moved:
            rnd += 1
            if p1:
                print(f'{rnd} {" ".join(str(zz) for zz in z)} {sum([(i+1)*j for i,j in enumerate(z)])}')
    if not p1:
        print(rnd)

with open(notes(2025,11,1)) as f:
    z = list(map(int,f.read().strip().split('\n')))
simulate(True)

with open(notes(2025,11,2)) as f:
    z = list(map(int,f.read().strip().split('\n')))
simulate(False)

with open(notes(2025,11,3)) as f:
    z = list(map(int,f.read().strip().split('\n')))
avg = sum(z)/len(z)
print(sum([zz - avg for zz in z if zz > avg]))

#!/usr/bin/pypy3
from math import prod
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def blocks(z,num):
    return sum(num//zz for zz in z)

with open(notes(2025,16,1)) as f:
    z = list(map(int,f.read().strip().split(',')))
print(blocks(z,90))

def scanzeros(wall):
    spell = []
    for i in range(1,len(wall)+1):
        if wall[i-1] > 0:
            newwall = wall
            for j in range(i-1,len(wall),i):
                newwall[j]-=1
            if all([a>=0 for a in newwall]):
                spell.append(i)
                wall = newwall
    return spell


with open(notes(2025,16,2)) as f:
    z = list(map(int,f.read().strip().split(',')))
print(prod(scanzeros(z)))

with open(notes(2025,16,3)) as f:
    z = list(map(int,f.read().strip().split(',')))
spell = scanzeros(z)
goal = 202520252025000
aim = 0
step = 1000000000000000
while step >= 1:
  for n in range(1,11):
    nstep = step*n
    if blocks(spell,aim + nstep) > goal:
       break
  aim += nstep-step
  step //= 10
print(aim,blocks(spell,aim))

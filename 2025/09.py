#!/usr/bin/pypy3
from itertools import combinations
from scipy.cluster.hierarchy import DisjointSet

def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def similarity(a,b):
    return sum(c==d for c,d in zip(a,b))

def findparents(i):
    a = z[i]
    for j,k in combinations(range(len(z)),2):
        if j == i or k == i:
            continue
        b = z[j]
        c = z[k]
        if all(a[j]==b[j] or a[j]==c[j] for j in range(len(a))):
            return j,k
    return None,None

with open(notes(2025,9,1)) as f:
    z = [zz.split(':')[1] for zz in f.read().strip().split('\n')]
print(similarity(z[2],z[0])*similarity(z[2],z[1]))

with open(notes(2025,9,2)) as f:
    z = [zz.split(':')[1] for zz in f.read().strip().split('\n')]
score = 0
for i in range(len(z)):
    j,k = findparents(i)
    if j is not None:
        score += similarity(z[i],z[j])*similarity(z[i],z[k])
print(score)

with open(notes(2025,9,3)) as f:
    z = [zz.split(':')[1] for zz in f.read().strip().split('\n')]
families = DisjointSet(list(range(len(z))))
for i in range(len(z)):
    j,k = findparents(i)
    if j is not None:
        families.merge(i,j)
        families.merge(i,k)
maxpoints = 0
maxlen = 0
for s in families.subsets():
    if len(s) > maxlen:
        maxlen = len(s)
        maxpoints = sum(s)+len(s)
print(maxpoints)

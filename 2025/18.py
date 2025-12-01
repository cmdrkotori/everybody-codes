#!/usr/bin/python3
from collections import defaultdict
import heapq
from copy import copy
import z3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def readinput(p):
    with open(notes(2025,18,p)) as f:
        z = f.read().strip().split('\n\n\n')
    zplants = z[0]
    plants = {}
    for pp in zplants.split('\n\n'):
        p = pp.split('\n')
        #Plant 1 with thickness 1
        #  0   1  2    3        4
        first_line = p[0].split()
        plant = int(first_line[1])
        plants[plant] = (int(first_line[4][:-1]), [])
        if 'free' in p[1]:
            #- free branch with thickness 1
            plants[plant][1].append((None, 1))
        else:
            #- branch to Plant 8 with thickness 28
            #0 1      2  3     4 5    6         7
            for line in range(1,len(p)):
                l = p[line].split()
                plants[plant][1].append((int(l[4]),int(l[7])))
    bits = []
    if len(z)>1:
        zbits = z[1]
        for array in zbits.split('\n'):
            bits.append(list(map(int,array.split())))
    return plants,bits

def energy(node):
    global tree
    plantthickness, branches = tree[node]
    if branches[0][0] is None:
        return plantthickness
    incoming = sum(energy(branch)*thickness for branch,thickness in branches)
    if incoming >= plantthickness:
        return incoming
    return 0

tree,bits = readinput(1)
print(energy(max(tree)))

def energybits(bits):
    global tree
    for i,b in enumerate(bits):
        tree[i+1] = (b,[(None, 1)])
    return energy(max(tree))

tree,bits = readinput(2)
s = 0
for testcase in bits:
    s += energybits(testcase)
print(s)

tree,bits = readinput(3)
sol = z3.Optimize()
powers = {}
for p in tree.keys():
    powers[p] = z3.Int(f'p_{p}')

for p,(thickness,branches) in tree.items():
    if branches == [(None, 1)]:
        sol.add(0 <= powers[p], powers[p] <= 1)
    else:
        incoming = sum(powers[branch]*branchthickness for branch,branchthickness in branches)
        sol.add(powers[p] == z3.If(incoming >= thickness, incoming, 0))

goal = powers[max(tree)]
sol.maximize(goal)
sol.check()
best = sol.model()[goal].as_long()

total = 0
for testcase in bits:
    result = energybits(testcase)
    if result != 0:
        total += best - result
print(total)

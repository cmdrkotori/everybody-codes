#!/usr/bin/pypy3
import math
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def p1():
    with open(notes(2025,4,1)) as f:
        z = list(map(int,f.read().strip().split('\n')))
    print(int(z[0]/z[-1]*2025))
p1()

def p2():
    with open(notes(2025,4,2)) as f:
        z = list(map(int,f.read().strip().split('\n')))
    print(math.ceil(10000000000000/(z[0]/z[-1])))
p2()

def p3():
    with open(notes(2025,4,3)) as f:
        z = f.read().strip().split('\n')
    gears = [(int(z[0]),int(z[0]))]
    gears.extend([tuple(map(int,g.split('|'))) for g in z[1:-2]])
    gears.extend([(int(z[-1]),int(z[-1]))])
    mul = 1
    for g in range(len(gears)-1):
        a,b = gears[g]
        c,d = gears[g+1]
        mul *= b/c
    print(int(100*mul))
p3()

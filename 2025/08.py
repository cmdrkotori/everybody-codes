#!/usr/bin/pypy3
from math import sin,cos,radians

def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

POINTSPERCIRCLE=256
point = []
for i in range(POINTSPERCIRCLE+1):
    theta = radians(i*360/POINTSPERCIRCLE)
    point.append((cos(theta),sin(theta)))

def intersects(x1,y1,x2,y2,x3,y3,x4,y4):
    ta = ((x1-x3)*(y3-y4)) - ((y1-y3)*(x3-x4))
    tb = ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4))
    ua = ((x1-x2)*(y1-y3)) - ((y1-y2)*(x1-x3))
    ub = ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4))
    if tb == 0 or ub == 0:
        return False
    t = ta/tb
    u = ua/-ub
    return t >= 0.00001 and t <= 0.99999 and u >= 0.00001 and u <= 0.99999

def pointintersects(a1,b1,a2,b2):
    a1,b1 = min(a1,b1),max(a1,b1)
    a2,b2 = min(a2,b2),max(a2,b2)
    if (a1,b1) == (a2,b2):
        return True
    x1,y1 = point[a1]
    x2,y2 = point[b1]
    x3,y3 = point[a2]
    x4,y4 = point[b2]
    return intersects(x1,y1,x2,y2,x3,y3,x4,y4)

with open(notes(2025,8,1)) as f:
    z = list(map(int,f.read().strip().split(',')))
inc = 0
for i in range(len(z)-1):
    a = z[i]
    b = z[i+1]
    if a == b+16 or a == b-16:
        inc += 1
print(inc)

with open(notes(2025,8,2)) as f:
    z = list(map(int,f.read().strip().split(',')))
segments=[]
def dosegments(p2):
    global z,segments
    inc = 0
    for i in range(len(z)-1):
        a = z[i]
        b = z[i+1]
        if p2:
            inc += sum([pointintersects(a,b,aa,bb) for aa,bb in segments])
        segments.append((a,b))
    return inc
print(dosegments(True))

with open(notes(2025,8,3)) as f:
    z = list(map(int,f.read().strip().split(',')))
inc = 0
segments=[]
dosegments(False)
possiblecuts=set()
for a in range(1,POINTSPERCIRCLE+1):
    for b in range(1,POINTSPERCIRCLE+1):
        if a != b:
            possiblecuts.add((min(a,b),max(a,b)))
maxcut = 0
for a,b in possiblecuts:
    cut = sum([pointintersects(a,b,aa,bb) for aa,bb in segments])
    if cut > maxcut:
        maxcut = cut
print(maxcut)

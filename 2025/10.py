#!/usr/bin/pypy3
from functools import cache

def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

mx,my = 0,0
def parsegrid(grid):
    global mx,my
    sheep = set()
    hideout = set()
    dragon = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                sheep.add((x,y))
            if grid[y][x] == 'D':
                dragon = (x,y)
            if grid[y][x] == '#':
                hideout.add((x,y))
    mx = len(grid[0])
    my = len(grid)
    return dragon,sheep,hideout

with open(notes(2025,10,1)) as f:
    z = f.read().strip().split('\n')
dragon,sheep,hideout = parsegrid(z)

moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
possible = set()
def movesfrom(x,y):
    for dx,dy in moves:
        if x + dx < mx and x + dx >= 0 and y + dy < my and y + dy >= 0:
            yield x+dx,y+dy
possible = set()
def domoves(dragon,remain):
    global possible
    if remain == 0:
        return
    x,y = dragon
    for xx,yy in movesfrom(x,y):
        possible.add((xx,yy))
        domoves((xx,yy),remain-1)
domoves(dragon,4)
inc = 0
for x,y in possible:
    if (x,y) in sheep:
        inc += 1
print(inc)

with open(notes(2025,10,2)) as f:
    z = f.read().strip().split('\n')
dragon,sheep,hideout = parsegrid(z)
def nextmoves(prevmoves):
    n = set()
    for x,y in prevmoves:
        for xx,yy in movesfrom(x,y):
            n.add((xx,yy))
    return n
def nextsheep(prevsheep):
    global hideout
    n = set()
    for x,y in prevsheep:
        nx,ny = x,y+1
        if ny < my:
            n.add((nx,ny))
    return n
def filtersheep(sheep,dragon,eaten):
    global hideout
    n = set()
    for x,y in sheep:
        if (x,y) not in dragon or (x,y) in hideout:
            n.add((x,y))
        else:
            eaten += 1
    return n,eaten
dmoves = [dragon]
nsheep = sheep
eaten = 0
for _ in range(20):
    dmoves = nextmoves(dmoves)
    nsheep,eaten = filtersheep(nsheep,dmoves,eaten)
    nsheep = nextsheep(nsheep)
    nsheep,eaten = filtersheep(nsheep,dmoves,eaten)
print(eaten)

with open(notes(2025,10,3)) as f:
    z = f.read().strip().split('\n')
dragon,sheep,hideout = parsegrid(z)

@cache
def dfs(dx,dy,sheep,sheepturn):
    global hideout
    wins = 0
    if len(sheep)==0:
        return 1
    if sheepturn:
        sheepmoved = False
        for sx,sy in sheep:
            nsheep = set(sheep)
            if sy + 1 == my:
                sheepmoved = True
                continue
            if (sx,sy+1) == (dx,dy) and (sx,sy+1) not in hideout:
                continue
            sheepmoved = True
            nsheep.remove((sx,sy))
            nsheep.add((sx,sy+1))
            wins += dfs(dx,dy,frozenset(nsheep),False)
        if not sheepmoved:
            wins += dfs(dx,dy,sheep,False)
    else:
        for x,y in movesfrom(dx,dy):
            nsheep = set(sheep)
            if (x,y) in nsheep and (x,y) not in hideout:
                nsheep.remove((x,y))
            wins += dfs(x,y,frozenset(nsheep),True)
    return wins
print(dfs(*dragon,frozenset(sheep),True))

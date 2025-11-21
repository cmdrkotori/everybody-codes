#!/usr/bin/pypy3
from collections import defaultdict
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

mx,my = 0,0
def parsegrid(z):
    global mx,my
    mx = len(z[0])
    my = len(z)
    grid = defaultdict(lambda: False)
    for x,r in enumerate(z):
        for y,c in enumerate(r):
            grid[x,y] = True if c == '#' else False
    return grid

def animate(grid):
    global mx,my
    dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
    ngrid = defaultdict(lambda: False)
    for y in range(my):
        for x in range(mx):
            tilesactive = 0
            for dx,dy in dirs:
                if grid[x+dx,y+dy]:
                    tilesactive += 1
            if grid[x,y]:
                ngrid[x,y] = tilesactive%2 == 1
            else:
                ngrid[x,y] = tilesactive%2 == 0
    return ngrid

def serialize(grid):
    global mx,my
    text = ''
    for y in range(my):
        for x in range(mx):
            text += '#' if grid[x,y] else '.'
        text += '\n'
    return text

def drawgrid(grid):
    print(serialize(grid))

def process(n):
    global grid
    s = 0
    for c in range(n):
        grid = animate(grid)
        s += sum(grid.values())
    print(s)

with open(notes(2025,14,1)) as f:
    z = f.read().strip().split('\n')
grid = parsegrid(z)
process(10)

with open(notes(2025,14,2)) as f:
    z = f.read().strip().split('\n')
grid = parsegrid(z)
process(2025)

with open(notes(2025,14,3)) as f:
    z = f.read().strip().split('\n')
target = parsegrid(z)
targetx = (34 - mx)//2
targety = (34 - my)//2
targetmx = mx
targetmy = my
mx = 34
my = 34
grid = defaultdict(lambda: False)

def checkmatch(grid):
    global target,target,targetx,targety,targetmx,targetmy
    for x in range(targetmx):
        for y in range(targetmy):
            if grid[x+targetx,y+targety] != target[x,y]:
                return False
    return True

cycle = 0
seen = set()
matches = []
while True:
    grid = animate(grid)
    s = serialize(grid)
    if s in seen:
        break
    seen.add(s)
    if checkmatch(grid):
        matches.append(sum(grid.values()))
    else:
        matches.append(0)
    cycle += 1
print(f'Found cycle length {cycle}!')
cyclelength = cycle
numrounds = 1000000000
numcycles = numrounds//cyclelength
cycleoffset = numrounds%cyclelength
s = sum(matches)*numcycles
for i in range(cycleoffset):
    s += matches[i]
print(s)

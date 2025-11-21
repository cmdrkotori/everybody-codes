#!/usr/bin/pypy3
from collections import defaultdict
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def parsegrid(z):
    grid = defaultdict(lambda: -1)
    for y,r in enumerate(z):
        for x,c in enumerate(r):
            grid[x,y] = int(c)
    return grid

def printgrid(z,seen):
    for y,r in enumerate(z):
        text = ''
        for x,c in enumerate(r):
            text += str(c) if (x,y) in seen else '.'
    print(text)

with open(notes(2025,12,1)) as f:
    z = f.read().strip().split('\n')
grid = parsegrid(z)
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def simulate(initial):
    seen = set(initial)
    todo = list(initial)
    while todo:
        x,y = todo.pop(0)
        seen.add((x,y))
        c = grid[x,y]
        if c == -1:
            continue
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            d = grid[nx,ny]
            if c >= d and (nx,ny) not in seen and d != -1:
                seen.add((nx,ny))
                todo.append((nx,ny))
    return seen
print(len(simulate([(0,0)])))


with open(notes(2025,12,2)) as f:
    z = f.read().strip().split('\n')
grid = parsegrid(z)
my = len(z)
mx = len(z[0])
print(len(simulate([(0,0),(mx-1,my-1)])))

with open(notes(2025,12,3)) as f:
    z = f.read().strip().split('\n')
grid = parsegrid(z)
my = len(z)
mx = len(z[0])

def findmax():
    mlseen = 0
    mseen = set()
    for x in range(mx):
        for y in range(my):
            seen = simulate([(x,y)])
            if len(seen) > mlseen:
                mlseen = len(seen)
                mseen = seen
    return mseen
seen = set()
for _ in range(3):
    seen = seen.union(findmax())
    for x,y in seen:
        grid[x,y] = -1
print(len(seen))

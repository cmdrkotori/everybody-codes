#!/usr/bin/pypy3
from collections import defaultdict
import heapq
from copy import copy
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def parsegrid(z,d):
    grid = defaultdict(lambda: d)
    xv,yv,sx,sy = None,None,None,None
    for y,r in enumerate(z):
        for x,c in enumerate(r):
            if c == '@':
                xv = x
                yv = y
                c = d
            if c == 'S':
                sx = x
                sy = y
                c = 0
            grid[x,y] = int(c)
    w = len(z[0])
    h = len(z)
    return xv,yv,w,h,grid,sx,sy

def checkme(xc,yc,xv,yv,r):
    return (xv-xc)**2 + (yv-yc)**2 <= r**2

def filtergrid(grid,w,h,xv,yv,r):
    for x in range(w):
        for y in range(h):
            if not checkme(x,y,xv,yv,r):
                grid[x,y] = 0
    return grid

def ifiltergrid(grid,w,h,xv,yv,r,c):
    for x in range(w):
        for y in range(h):
            if checkme(x,y,xv,yv,r):
                grid[x,y] = c
    return grid

def printgrid(grid,w,h,r,d,c,path):
    print(f'\nR: {r}  D: {d}')
    for y in range(h):
        text = ''
        for x in range(w):
            if (x,y) in path:
                text += '#'
            elif grid[x,y] == c:
                text += '.'
            else:
                text += str(grid[x,y])
        print(text)

with open(notes(2025,17,1)) as f:
    z = f.read().strip().split('\n')
xv,yv,w,h,grid,sx,sy = parsegrid(z,0)
grid = filtergrid(grid,w,h,xv,yv,10)
print(sum(grid.values()))

with open(notes(2025,17,2)) as f:
    z = f.read().strip().split('\n')
xv,yv,w,h,grid,sx,sy = parsegrid(z,0)
maxd = 0
maxdr = 0
lastval = sum(grid.values())
for r in range(1,1+(w-1)//2):
    grid = ifiltergrid(grid,w,h,xv,yv,r,0)
    val = sum(grid.values())
    d = lastval - val
    lastval = val
    if d > maxd:
        maxd = d
        maxdr = r
print(maxd,maxdr,maxd*maxdr)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def costtotarget(grid,w,h,sx,sy,sc,spath,tx,ty,stops):
    queue = [(sc,sx,sy,spath)]
    seen = set()
    while queue:
        c,px,py,path = heapq.heappop(queue)
        for dx,dy in dirs:
            nx,ny = px+dx,py+dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if (nx,ny) in stops:
                continue
            npath = copy(path)
            npath.append((nx,ny))
            if (nx,ny) == (tx,ty):
                return c+grid[nx,ny],npath
            if (nx,ny) in seen:
                continue
            seen.add((nx,ny))
            heapq.heappush(queue,(c+grid[nx,ny],nx,ny,npath))

def costtodest(grid,w,h,src,dest,stops):
    costatdest = {}
    for x,y in dest:
        costatdest[x,y] = 1e10,list()
    for p,pp in src.items():
        sx,sy = p
        pc,spath = pp
        for tx,ty in dest:
            c,p = costtotarget(grid,w,h,sx,sy,pc,spath,tx,ty,stops)
            oc,op = costatdest[x,y]
            if c < oc:
                costatdest[tx,ty] = (c,p)
    return costatdest

with open(notes(2025,17,3)) as f:
    z = f.read().strip().split('\n')
xv,yv,w,h,grid,sx,sy = parsegrid(z,1e10)

print(f'Center at {xv},{yv}')
print(f'Start at {sx},{sy}')
r = 1
for r in range(1,(w-1)//2):
    print(f'Trying radius {r}')
    grid = ifiltergrid(grid,w,h,xv,yv,r,1e10)
    src = {(sx,sy):(0,[(sx,sy)])}

    left = set([(x,yv) for x in range(0,xv-r)])
    right = set([(x,yv) for x in range(xv+r+1,w)])
    top = set([(xv,y) for y in range(0,yv-r)])
    bottom = set([(xv,y) for y in range(yv+r+1,h)])

    costatdest = costtodest(grid,w,h,src,bottom,right)
    mincost = 1e12
    minpath = list()
    for p,pp in costatdest.items():
        px,py = p
        pc,ppath = pp
        c,path = costtotarget(grid,w,h,px,py,pc,ppath,sx,sy,left)
        if c < mincost:
            mincost = c
            minpath = path
    s = 0
    for x,y in minpath:
        s += grid[x,y]
    printgrid(grid,w,h,r,c,1e10,minpath)
    if s < (r+1)*30:
        break
print(s*r)

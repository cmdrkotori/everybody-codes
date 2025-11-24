#!/usr/bin/pypy3
import heapq
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def parsemaze(z):
    x,y = 0,0
    dx,dy = 0,-1
    walls = []
    diagsx = set([-1,0,1])
    diagsy = set([-1,0,1])
    for d,dd in z:
        if d == 'L':
            #  L: 0,-1 -> -1,0   1,0 -> 0,-1
            dx,dy = dy,-dx
        else:
            #  R: -1,0 -> 0,-1   0,-1 -> 1,0
            dx,dy = -dy,dx
        nx = x + dd*dx
        ny = y + dd*dy
        walls.append((min(x,nx),min(y,ny),max(x,nx),max(y,ny),dd))
        for ix in range(-1,2):
            diagsx.add(ix+nx)
            diagsx.add(ix+x)
        for iy in range(-1,2):
            diagsy.add(iy+ny)
            diagsy.add(iy+y)
        x,y = nx,ny
    return x,y,walls,sorted(list(diagsx)),sorted(list(diagsy))

def intersects(x,y,wall):
    wx,wy,nx,ny,dd = wall
    if nx-wx == 0:
        return wy <= y <= ny and x==wx
    return wx <= x <= nx and y == wy

def intersectsany(x,y,walls):
    for wall in walls:
        if intersects(x,y,wall):
            return True
    return False

def findzero(diag):
    for ix in range(len(diag)):
        if diag[ix] == 0:
            return ix
    return None

def bfs(targetx,targety,walls,diagsx,diagsy):
    ix = findzero(diagsx)
    iy = findzero(diagsy)
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    h = [(0,ix,iy,0,0)]
    seen = set([0,0])
    while True:
        steps,ix,iy,x,y = heapq.heappop(h)
        for dx,dy in dirs:
            nix,niy = ix+dx,iy+dy
            if nix < 0 or nix >= len(diagsx) or niy < 0 or niy >= len(diagsy):
                continue
            nx,ny = diagsx[nix],diagsy[niy]
            dsteps = abs(nx-x)+abs(ny-y)
            if (nx,ny) == (targetx,targety):
                return steps+dsteps
            if (nx,ny) in seen:
                continue
            if intersectsany(nx,ny,walls):
                continue
            seen.add((nx,ny))
            heapq.heappush(h,(steps+dsteps,nix,niy,nx,ny))

def dopart(p):
    with open(notes(2025,15,p)) as f:
        z = [(x[0], int(x[1:])) for x in f.read().strip().split(',')]
    targetx,targety,walls,diagsx,diagsy = parsemaze(z)
    print(bfs(targetx,targety,walls,diagsx,diagsy))

dopart(1)
dopart(2)
dopart(3)

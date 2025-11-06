#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def add(x1,y1,x2,y2):
    return x1+x2,y1+y2

def mul(x1,y1,x2,y2):
    return x1*x2 - y1*y2, x1*y2 + y1*x2

def div(x1,y1,x2,y2):
    return int(x1/x2), int(y1/y2)

def p1():
    with open(notes(2025,2,1)) as f:
        z = f.read().strip()
    ax,ay = map(int,z[3:-1].split(','))
    x,y = 0,0
    for _ in range(3):
        x,y = mul(x,y,x,y)
        x,y = div(x,y,10,10)
        x,y = add(x,y,ax,ay)
    print(f'[{x},{y}]')
p1()

def p2(d1,d2,part):
    with open(notes(2025,2,part)) as f:
        z = f.read().strip()
    ax,ay = map(int,z[3:-1].split(','))
    def dopoint(xx,yy):
        x,y=0,0
        for _ in range(100):
            x,y = mul(x,y,x,y)
            x,y = div(x,y,100000,100000)
            x,y = add(x,y,xx,yy)
            if x > 1000000 or x < -1000000 or y > 1000000 or y < -1000000:
                break
        return x <= 1000000 and x >= -1000000 and y <= 1000000 and y >= -1000000
    engraved = 0
    for ix in range(d1):
        for iy in range(d1):
            x,y = ix*d2+ax,iy*d2+ay
            if dopoint(x,y):
                engraved += 1
    print(engraved)
p2(101,10,2)
p2(1001,1,3)

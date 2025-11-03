#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def pcreature(x):
    match x:
        case 'A':
            return 0
        case 'B':
            return 1
        case 'C':
            return 3
        case 'D':
            return 5
    return 0

def extrax(x):
    match x:
        case 3:
            return 0
        case 2:
            return 0
        case 1:
            return 2
        case 0:
            return 6

def p1():
    with open(notes(2024,1,1)) as f:
        data = f.read().strip()
    p = 0
    for d in data:
        p += pcreature(d)
    print(p)

def p2():
    with open(notes(2024,1,2)) as f:
        data = f.read().strip()
    p = 0
    for i in range(len(data)//2):
        x,y = data[i*2], data[i*2+1]
        dp = 0
        nx = f'{x}{y}x'.count('x')
        dp = pcreature(x) + pcreature(y) + extrax(nx)
        p += dp
    print(p)


def p3():
    with open(notes(2024,1,3)) as f:
        data = f.read().strip()
    pp = []
    for p in range(len(data)//3):
        x,y,z = data[p*3], data[p*3+1], data[p*3+2]
        nx = f'{x}{y}{z}'.count('x')
        dp = pcreature(x) + pcreature(y) + pcreature(z) + extrax(nx)
        pp.append(dp)
    print(sum(pp))

p1()
p2()
p3()

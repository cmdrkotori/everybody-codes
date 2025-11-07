#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def p1():
    with open(notes(2025,3,1)) as f:
        z = list(map(int,f.read().strip().split(',')))
    z.sort()
    last = 0
    s = 0
    for crate in z:
        if crate == last:
            continue
        s += crate
        last = crate
    print(s)
p1()

def p2():
    with open(notes(2025,3,2)) as f:
        z = list(map(int,f.read().strip().split(',')))
    z.sort()
    last = 0
    s = 0
    num = 0
    for crate in z:
        if crate == last:
            continue
        s += crate
        last = crate
        num += 1
        if num == 20:
            break
    print(s)
p2()

def p3():
    with open(notes(2025,3,3)) as f:
        leftover = list(map(int,f.read().strip().split(',')))
    leftover.sort()
    num = 0
    while leftover:
        last = 0
        remaining = []
        leftover.sort()
        for crate in leftover:
            if crate == last:
                remaining.append(crate)
                continue
            last = crate
        leftover = remaining
        num += 1
    print(num)
p3()

#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def p(part):
    with open(notes(2025,1,part)) as f:
        d1,d2 = f.read().strip().split('\n\n')
    names = d1.split(',')
    moves = d2.split(',')
    index = 0
    for m in moves:
        a,b = m[0],int(m[1:])
        delta = -b if a == 'L' else b
        if part == 1:
                index = max(0, min(index+delta, len(names)-1))
        if part == 2:
                index += delta
                index %= len(names)
        if part == 3:
                delta %= len(names)
                names[delta],names[0] = names[0],names[delta]
    print(names[index])
p(1)
p(2)
p(3)

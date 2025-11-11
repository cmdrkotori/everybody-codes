#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def docat(men,mentor,novice):
    pairs = 0
    mentors = 0
    possible = mentor+novice
    for m in men:
        if m not in possible:
            continue
        if m == mentor:
            mentors += 1
        if m == novice:
            pairs += mentors
    return pairs

def p1():
    with open(notes(2025,6,1)) as f:
        men = f.read().strip()
    print(docat(men,'A','a'))
p1()

def p2():
    with open(notes(2025,6,2)) as f:
        men = f.read().strip()
    print(docat(men,'A','a') + docat(men,'B','b') + docat(men,'C','c'))
p2()

def donovice(r,mentor):
    return sum([rr==mentor for rr in r])

def dototal(men,number,dist):
    total = men*number
    p = 0
    for i in range(len(total)):
        if total[i] in 'abc':
            r = total[max(0,i-dist):min(len(total),i+dist+1)]
            if total[i] == 'a':
                p += donovice(r,'A')
            if total[i] == 'b':
                p += donovice(r,'B')
            if total[i] == 'c':
                p += donovice(r,'C')
    return p

def p3():
    with open(notes(2025,6,3)) as f:
        men = f.read().strip()
    print(dototal(men,1000,1000))
p3()

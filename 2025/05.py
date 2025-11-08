#!/usr/bin/pypy3
from functools import cmp_to_key
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def dosword(index,numbers):
    fishbone = [[numbers[0],(),()]]
    def findbone(n):
        for j in range(len(fishbone)):
            if n < fishbone[j][0] and not fishbone[j][1]:
                fishbone[j][1] = n
                return
            if n > fishbone[j][0] and not fishbone[j][2]:
                fishbone[j][2] = n
                return
        fishbone.append([n,(),()])

    for i in range(1,len(numbers)):
        findbone(numbers[i])
    return index,int(''.join([f'{x[0]}' for x in fishbone])),fishbone

def p1():
    with open(notes(2025,5,1)) as f:
        z = f.read().strip()
    #z='58:5,3,7,8,9,10,4,5,7,8,8'
    index,numbers = z.split(':')
    numbers = list(map(int,numbers.split(',')))
    index,strength,fishbone = dosword(int(index),numbers)
    print(strength)
p1()

def p2():
    with open(notes(2025,5,2)) as f:
        swords = f.read().strip().split('\n')
    mx,mn = (),()
    for z in swords:
        index,numbers = z.split(':')
        numbers = list(map(int,numbers.split(',')))
        index,strength,fishbone = dosword(int(index),numbers)
        if not mx or strength > mx:
            mx = strength
        if not mn or strength < mn:
            mn = strength
    print(mx-mn)
p2()

def p3():
    with open(notes(2025,5,3)) as f:
        sw = f.read().strip().split('\n')
    mx,mn = (),()
    swords = []
    for z in sw:
        index,numbers = z.split(':')
        numbers = list(map(int,numbers.split(',')))
        swords.append(dosword(int(index),numbers))
    def swordcmp(a,b):
        i1,s1,f1 = a
        i2,s2,f2 = b
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1
        def dolevel(l):
            score = ''
            if l[1]:
                score += str(l[1])
            score += str(l[0])
            if l[2]:
                score += str(l[2])
            return int(score)
        for x in range(len(f1)):
            l1 = dolevel(f1[x])
            l2 = dolevel(f2[x])
            if l1 < l2:
                return -1
            if l1 > l2:
                return 1
        if i1 < i2:
            return -1
        if i1 > i2:
            return 1
        return 0
    swords.sort(key=cmp_to_key(swordcmp),reverse=True)
    score = 0
    for x in range(len(swords)):
        i,s,f = swords[x]
        score += i*(x+1)
    print(score)
p3()

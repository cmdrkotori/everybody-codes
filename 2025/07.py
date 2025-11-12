#!/usr/bin/pypy3
def notes(year,day,part):
    return f'everybody_codes_e{year}_q{day:02}_p{part}.txt'

def makerule(rules):
    rules = rules.split('\n')
    rules = [r.split(' > ') for r in rules]
    rule = {}
    for r in rules:
        rule[r[0]] = r[1].split(',')
    return rule

def p12(p2):
    with open(notes(2025,7,2 if p2 else 1)) as f:
        names,rules = f.read().strip().split('\n\n')
    names = names.split(',')
    rule=makerule(rules)
    s = 0
    for i,n in enumerate(names,start=1):
        for x in range(len(n)-1):
            if n[x] not in rule:
                break
            if n[x+1] not in rule[n[x]]:
                break
            if x == len(n)-2:
                if not p2:
                    print(n)
                s += i
    if p2:
        print(s)
p12(False)
p12(True)

with open(notes(2025,7,3)) as f:
    names,rules = f.read().strip().split('\n\n')
names = names.split(',')
rule=makerule(rules)
newnames = set()
def findnames(prefix):
    for pi in range(len(prefix)-1):
        if prefix[pi+1] not in rule[prefix[pi]]:
            return 0
    todo = [prefix]
    namesfound = 0
    while todo:
        p = todo.pop(0)
        if p[-1] not in rule:
            continue
        for r in rule[p[-1]]:
            newname = p + r
            if newname in newnames:
                continue
            if len(newname) >= 7:
                namesfound += 1
                newnames.add(newname)
            if len(newname) <= 10:
                todo.append(newname)
    return namesfound
print(sum([findnames(n) for n in names]))

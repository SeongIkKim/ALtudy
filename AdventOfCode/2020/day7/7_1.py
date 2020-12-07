from collections import defaultdict

with open('inputs.txt') as f:
    rules = f.read().split('\n')[:-1]

rules_d = defaultdict(set)

for rule in rules:
    outer, inner = rule.split(' contain ')
    outer = ' '.join(outer.split()[:-1])
    inner = inner.split(',')

    for i in range(len(inner)):
        inner[i] = ' '.join(inner[i].split()[1:3])

    if inner[0][:5] != 'other':
        for i in inner:
            rules_d[i].add(outer)

outers= set()


def search(d, target, outers):
    for i in d[target]:
        search(d,i,outers)
        outers.add(i)

search(rules_d, 'shiny gold', outers)

print(len(outers))



# dfs 문제다!

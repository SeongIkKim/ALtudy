from collections import defaultdict

with open('inputs.txt') as f:
    rules = f.read().split('\n')[:-1]

rules_number = defaultdict(list)

for rule in rules:
    outer, inner = rule.split(' contain ')
    outer = ' '.join(outer.split()[:-1])
    inner = inner.split(',')

    for i in range(len(inner)):
        number = name = None
        words = inner[i].split()[:3]
        name = ' '.join(words[1:])
        if words[0].isdigit():
            number = int(words[0])
            rules_number[outer].append((name,number))
        inner[i] = name



count = 0
for k, v in rules_number.items():
    print(k, v)

def count_bags(d, target):
    print(f'im in target {target}')
    if not d[target]:
        print('it contains nothing')
        return 1
    a = 0
    for require in d[target]:
        name, num = require[0], require[1]
        print(f"I'll gonna check how much bags {name} has...")
        b = (num * (count_bags(d, name)))
        print(f"it has {b} bags")
        a += b

    print('all a is ', a)

    return a + 1

count = count_bags(rules_number, 'shiny gold') - 1

print(count)


# def search(d, target, count):
#     for i in d[target]:
#         search(d, i, outers)
#         outers.add(i)



# search(rules_d, 'shiny gold', count)

# dfs 문제다!

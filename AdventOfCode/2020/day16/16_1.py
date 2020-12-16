import re

with open('inputs.txt') as f:
    rules, mine, nearby = f.read().strip().split('\n\n')

rules = rules.split('\n')
fields =[]

# field range 따로 구해서 모아두기
ranges = []
for rule in rules:
    field, ran = rule.split(': ')
    fields.append(field)
    rans = ran.split(' or ')
    for r in rans:
        start, end = [int(i) for i in r.split('-')]
        ranges.append(range(start, end+1))

# nearby tickets 숫자 구하기
nb_nums = [int(i) for i in re.split('\D+', nearby)[1:]]

# 올바른 범위 숫자 set S
S = set()
for r in ranges:
    S = S.union(set(r))

# 유효성 검사
ans = 0
for num in nb_nums:
    if num not in S:
        ans += num

print(ans)




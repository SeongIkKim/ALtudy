from collections import defaultdict

with open('inputs.txt') as f:
    rules, mine, nearby = f.read().strip().split('\n\n')

# 내 티켓 정리
mine = mine.split('\n')[1].split(',')

rules = rules.split('\n')
fields =[]

# field range 따로 구해서 모아두기
ranges = []
ran_d = defaultdict(set)
for rule in rules:
    field, ran = rule.split(': ')
    fields.append(field)
    rans = ran.split(' or ')
    for r in rans:
        start, end = [int(i) for i in r.split('-')]
        this_range = range(start, end+1)
        ranges.append(this_range)
        ran_d[field] |= set(this_range) # 합집합으로 업데이트

# nearby tickets 분리
tickets = [i for i in nearby.split('\n')][1:]
for i in range(len(tickets)):
    tickets[i] = [int(num) for num in tickets[i].split(',')]

# 올바른 범위 숫자 set S
S = set()
for r in ranges:
    S = S.union(set(r))

# 티켓 솎아내기
tickets = [ticket for ticket in tickets if set(ticket).issubset(S)]

# 티켓 필드별로 정리
t_d = defaultdict(list)
for c in range(len(tickets[0])):
    t_d[c] = [ticket[c] for ticket in tickets]

# 유효성 검사
candidates = defaultdict(set)
for column, data in t_d.items():
    for field, field_ran in ran_d.items():
        # print(data, '###', field, field_ran, end='')
        if set(data).issubset(field_ran):
            # print('가능', end='')
            candidates[column].add(field)
        # print('')

ans = defaultdict(str)
while fields:
    for c,f in candidates.items():
        if len(set(fields) & f) == 1:
            ans[c] = (set(fields)&f).pop()
            fields.remove(ans[c])

value = 1
for k,v in ans.items():
    if v.startswith('departure'):
        value *= int(mine[k])

print(value)
















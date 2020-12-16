
from collections import defaultdict

with open('inputs.txt') as f:
    groups = f.read().strip().split('\n\n')

answer_for_everyone = []

for group in groups:
    group = group.split()
    headcount = len(group)
    answer_dict = defaultdict(int)
    for answers in group:
        for answer in answers:
            answer_dict[answer] += 1
    count = 0
    for v in answer_dict.values():
        if v == headcount:
            count+=1
    answer_for_everyone.append(count)

print(sum(answer_for_everyone))

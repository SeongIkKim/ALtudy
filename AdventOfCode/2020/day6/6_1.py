with open('inputs.txt') as f:
    forms = f.read().strip().split('\n\n')

group_answers = []

for form in forms:
    form = form.split()
    group_answer = set()
    for answers in form:
        for answer in answers:
            group_answer.add(answer)
    group_answers.append(group_answer)

count = 0

for i in group_answers:
    count += len(i)

print(count)


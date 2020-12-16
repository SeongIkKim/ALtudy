import re

with open('inputs.txt') as f:
    candidate_group = f.read().split('\n')[:-1]

count = 0

for candidate in candidate_group:
    time_s, letter_s, password = candidate.split()
    least,most = time_s.split('-')
    letter = letter_s[0]

    if int(least) <= len(re.findall(letter,password)) <= int(most):
        count += 1

print(count)

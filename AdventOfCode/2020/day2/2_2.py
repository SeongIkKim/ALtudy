import re

with open('inputs.txt') as f:
    candidate_group = f.read().split('\n')[:-1]

count = 0

for candidate in candidate_group:
    time_s, letter_s, password = candidate.split()
    first,second = map(int, time_s.split('-'))
    letter = letter_s[0]

    if len(re.findall(letter,password[first-1]+password[second-1])) == 1:
        count+=1

print(count)

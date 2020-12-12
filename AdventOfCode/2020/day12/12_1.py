from collections import defaultdict

with open('inputs.txt') as f:
    S = f.read().strip().split('\n')

direction = {0:'N', 90:'E', 180:'S', 270:'W'}
direction.update({v:k for k,v in direction.items()}) # k, v 뒤집기
f = 90
d = {'E':0, 'W':0, 'N':0, 'S':0}

for line in S:
    i,val = line[0], int(line[1:])
    print(i, val)
    if i == 'F':
        d[direction[f]] += val
    elif i in d.keys():
        d[i] += val
    elif i == 'L':
        ab = f-val
        f = 360+ab if ab<0 else ab
        print(f)
    elif i == 'R':
        f = (f+val)%360

answer = (abs(d['E']-d['W'])) + (abs(d['N']-d['S']))
print(answer)

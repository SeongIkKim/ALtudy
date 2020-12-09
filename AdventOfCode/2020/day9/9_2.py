from collections import deque

with open('inputs.txt') as f:
    N = f.read().split('\n')[:-1]

N = [int(i) for i in N]
dq = deque()
preamble = 25

for i in range(preamble):
    dq.append(N[i])

i+=1

while i < len(N):
    exist = False
    for num in dq:
        if N[i] - num in dq:
            exist = True
            break
    if not exist:
        print(N[i])
        break
    dq.popleft()
    dq.append(N[i])
    i+=1

invalid_num = N[i]

for j in range(i,0,-1):
    for k in range(j-1,-1,-1):
        if sum(N[k:j]) == invalid_num:
            print(min(N[k:j])+ max((N[k:j])))
            break
        elif sum(N[k:j]) > invalid_num:
            break

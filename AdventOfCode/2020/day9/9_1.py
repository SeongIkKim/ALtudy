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


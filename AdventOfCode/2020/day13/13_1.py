with open('inputs.txt') as f:
    ets, ids = f.read().strip().split('\n')

ids = set(int(ID) for ID in ids.split(',') if ID != 'x')

root = ets = int(ets)
done = False

while not done:
    for ID in ids:
        if ets % ID == 0:
            print(ID)
            done = True
            break
    ets += 1

print(ID * (ets-1 - root))

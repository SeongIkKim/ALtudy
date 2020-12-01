with open('inputs.txt') as f:
    entries = [int(entry) for entry in (f.read().split('\n'))[:-1]]

entries.sort()

done = False

for i in range(len(entries)):
    ap = i+1
    bp = len(entries)-1
    while ap < bp:
        a, b, c = entries[ap], entries[bp], entries[i]
        if a+b+c > 2020:
            bp -= 1
        elif a+b+c < 2020:
            ap += 1
        else:
            print(a,b,c, a*b*c)
            done=True
            break
    if done:
        break






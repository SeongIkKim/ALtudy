with open('inputs.txt') as f:
    program = f.read().split('\n')[:-1]

acc = i = 0
visited = []
while i not in visited:
    visited.append(i)
    op, arg = program[i].split()
    # print(op,arg)
    if op == 'nop':
        i += 1
    elif op == 'acc':
        acc += int(arg)
        i += 1
    elif op == 'jmp':
        i += int(arg)

print(acc)

with open('inputs.txt') as f:
    tree_map = f.read().split('\n')[:-1]

candidates = [(1,1),(3,1),(5,1),(7,1),(1,2)]

answer = 1
for candidate in candidates:
    r = 0
    c = 0
    counter = 0
    while r < len(tree_map)-1:
        c += candidate[0]
        r += candidate[1]
        if tree_map[r][c % len(tree_map[r])] == '#':
            counter += 1
    answer *= counter

print(answer)

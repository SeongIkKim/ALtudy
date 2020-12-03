with open('inputs.txt') as f:
    tree_map = f.read().split('\n')[:-1]

r = 0
c = 0
counter = 0

while r < len(tree_map)-1:
    c += 3
    r += 1
    if tree_map[r][c % len(tree_map[r])] == '#':
        counter += 1

print(counter)

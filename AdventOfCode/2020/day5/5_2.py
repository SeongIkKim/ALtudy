with open('inputs.txt') as f:
    passes = f.read().split('\n')[:-1]

ids = []

for p in passes:
    r = 0
    c = 0

    row = range(128)
    column = range(8)

    for i in range(7):
        if p[i] == 'F':
            row = row[:len(row)//2]
        else:
            row = row[len(row)//2:]

    if row[0] != row[-1]:
        print('Error')
    r = row[0]

    for i in range(-3,1):
        if p[i] == 'L':
            column = column[:len(column)//2]
        else:
            column = column[len(column)//2:]

    if column[0] != column[-1]:
        print('Error')
    c = column[0]

    ids.append(r*8 + c)

for i in range(894):
    if i not in ids:
        print(i)



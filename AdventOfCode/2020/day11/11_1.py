with open('inputs.txt') as f:
    map = f.read().strip().split('\n')

rs = len(map)
cs = len(map[0])

def count_adjacent_seats(r,c,map):
    count = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if i == r and j == c :
                continue
            if map[i][j] == '#':
                count +=1
    return count

change = True

while change:
    change = False

    # map 세팅
    for i in range(len(map)):
        map[i] = ''.join(['.', map[i], '.'])

    map.insert(0, '.' * len(map[0]))
    map.append('.' * len(map[0]))

    # new_map 초기화
    new_map = []


    for i in range(1, rs+1):
        s = ''
        for j in range(1, cs+1):
            count = count_adjacent_seats(i,j, map)
            status = map[i][j]

            if count >=4 and status == '#':
                s = ''.join([s,'L'])
                change = True
            elif not count and status == 'L':
                s = ''.join([s, '#'])
                change = True
            else:
                s = ''.join([s, status])


        new_map.append(s)

    map = new_map

oc = 0

for line in map:
    for ch in line:
        if ch == '#':
            oc += 1

print(oc)




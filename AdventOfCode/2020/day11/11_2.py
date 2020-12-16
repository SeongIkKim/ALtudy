with open('inputs.txt') as f:
    map = f.read().strip().split('\n')

rs = len(map)
cs = len(map[0])

# for i in map:
#     print(i)

def count_adjacent_seats(r,c,rs,cs,map):

    count = 0
    # 좌
    for i in range(c-1,-1,-1):
        try:
            if map[r][i] != '.':
                if map[r][i] == '#':
                    count+=1
                    # print('좌', end=' ')
                break
        except:
            break
    # 우
    for i in range(c+1,cs):
        try:
            if map[r][i] != '.':
                if map[r][i] == '#':
                    count += 1
                    # print('우', end=' ')
                break
        except:
            break
    # 상
    for i in range(r-1,-1,-1):
        try:
            if map[i][c] != '.':
                if map[i][c] == '#':
                    count+=1
                    # print('상', end=' ')
                break
        except:
            break

    # 하
    for i in range(r+1,rs):
        try:
            if map[i][c] != '.':
                if map[i][c] == '#':
                    count+=1
                    # print('하', end=' ')
                break
        except:
            break
    # 좌상대각
    dot = (r-1,c-1)
    while dot[0]>=0 and dot[1]>=0:
        try:
            if map[dot[0]][dot[1]] != '.':
                if map[dot[0]][dot[1]] == '#':
                    count += 1
                    # print('좌상', end=' ')
                break
            dot = (dot[0] - 1, dot[1] - 1)
        except:
            break
    # 우하대각
    dot = (r+1, c+1)
    while dot[0]<=rs and dot[1]<=cs:
        try:
            if map[dot[0]][dot[1]] != '.':
                if map[dot[0]][dot[1]] == '#':
                    count += 1
                    # print('우하', end=' ')
                break
            dot = (dot[0] + 1, dot[1] + 1)
        except:
            break
    # 우상대각
    dot = (r-1, c+1)
    while dot[0]>=0 and dot[1]>=0:
        try:
            if map[dot[0]][dot[1]] != '.':
                if map[dot[0]][dot[1]] == '#':
                    count += 1
                    # print('우상', end=' ')
                break
            dot = (dot[0] - 1, dot[1] + 1)
        except:
            break
    # 좌하대각
    dot = (r+1, c-1)
    while dot[0]>=0 and dot[1]>=0:
        try:
            if map[dot[0]][dot[1]] != '.':
                if map[dot[0]][dot[1]] == '#':
                    count += 1
                    # print('좌하', end=' ')
                break
            dot = (dot[0] + 1, dot[1] - 1)
        except:
            break
    # if count>=5:
        # print('change')
    # print('')
    return count

change = True

while change:
# for i in range(1):
    change = False

    # new_map 초기화
    new_map = []


    for i in range(rs):
        s = ''
        for j in range(cs):
            status = map[i][j]
            if status == '.':
                s = ''.join([s, status])
                continue
            count = count_adjacent_seats(i,j,rs,cs, map)
            # print((i,j),status, count)

            if count >=5 and status == '#':
                s = ''.join([s,'L'])
                change = True
            elif not count and status == 'L':
                s = ''.join([s, '#'])
                change = True
            else:
                s = ''.join([s, status])


        new_map.append(s)

    map = new_map

    # for i in map:
        # print(i)
    # print('-----1턴종료--------')


oc = 0

for line in map:
    for ch in line:
        if ch == '#':
            oc += 1

print(oc)


'''
N queen인지 백트래킹인지 dfs인지 모르겠는데..
배우고 와서 혼쭐내준다 너...
'''

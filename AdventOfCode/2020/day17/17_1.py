from collections import deque

with open('inputs.txt') as f:
    cube = deque([f.read().strip().split('\n')])


def check_neighbor(cube, xp, yp, zp):
    check = 0 # 주위의 active 개수
    for x in range(xp-1,xp+2):
        for y in range(yp-1,yp+2):
            for z in range(zp-1,zp+2):
                try:
                    if x==xp and y==yp and z==zp :
                        continue
                    if cube[z][y][x] == '#':
                        check +=1
                except:
                    continue
    # print(f"({x},{y},{z}):{check}개")
    return check

def change_status(cube,new_cube,xp, yp, zp):
    check = check_neighbor(cube, xp, yp, zp)
    if cube[zp][yp][xp] == '#':
        if check < 2 or check > 3:
            new_cube[zp][yp][xp] = '.'
    else :
        if check == 3:
            new_cube[zp][yp][xp] = '#'

# for _ in range(6):
for i in range(1,7):
    print (f"After {i} cycles")

    # 패딩 추가 코드
    for dimension in cube:
        for i in range(len(dimension)):
            dimension[i] = '.' + dimension[i] + '.'
        dimension.insert(0, '.' * len(dimension[0]))
        dimension.append('.' * len(dimension[0]))
    pad_dimension = ['.'*len(cube[0][0])]*len(cube[0])
    cube.appendleft(pad_dimension)
    cube.append(pad_dimension)

    new_cube = deque()
    for dimension in cube:
        nd = []
        for i in range(len(dimension)):
            nd.append([status for status in dimension[i]])
        new_cube.append(nd)

    # 변환 코드
    for z in range(len(cube)):
        for y in range(len(cube[0])):
            for x in range(len(cube[0][0])):
                change_status(cube,new_cube,x,y,z)
            new_cube[z][y] = ''.join(new_cube[z][y])


    cube = new_cube

    # # 출력 코드
    # mid = len(cube) // 2
    # for dimension in cube:
    #     print('z=', cube.index(dimension) - mid)  # 차원 높이
    #     for row in dimension:
    #         print(row)


count = 0
for z in range(len(cube)):
    for y in range(len(cube[0])):
        for x in range(len(cube[0][0])):
            if cube[z][y][x] == '#':
                count+=1

print(count)


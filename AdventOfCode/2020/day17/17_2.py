from collections import deque

with open('inputs.txt') as f:
    cube = deque([[f.read().strip().split('\n')]])


def check_neighbor(cube, xp, yp, zp, wp):
    check = 0 # 주위의 active 개수
    for w in range(wp-1, wp+2):
        for x in range(xp-1,xp+2):
            for y in range(yp-1,yp+2):
                for z in range(zp-1,zp+2):
                    try:
                        if x==xp and y==yp and z==zp and w==wp :
                            continue
                        if cube[w][z][y][x] == '#':
                            check +=1
                        ### 추가
                        if check>4 :
                            break
                        ### 추가 끝
                    except:
                        continue
    # print(f"({x},{y},{z}):{check}개")
    return check

def change_status(cube,new_cube,xp, yp, zp, wp):
    check = check_neighbor(cube, xp, yp, zp, wp)
    if cube[wp][zp][yp][xp] == '#':
        if check < 2 or check > 3:
            new_cube[wp][zp][yp][xp] = '.'
    else :
        if check == 3:
            new_cube[wp][zp][yp][xp] = '#'

# # for _ in range(6):
for i in range(1,7):
    print (f"After {i} cycles")

    # 패딩 추가 코드
    for hyper in cube:
        for dimension in hyper:
            for i in range(len(dimension)):
                dimension[i] = '.' + dimension[i] + '.'
            dimension.insert(0, '.' * len(dimension[0]))
            dimension.append('.' * len(dimension[0]))
        pad_dimension = ['.'*len(dimension[0])]*len(hyper[0])
        hyper.insert(0,pad_dimension)
        hyper.append(pad_dimension)
    pad_hyper = [['.' * len(dimension[0])] *len(hyper[0])]  *len(cube[0])
    cube.appendleft(pad_hyper)
    cube.append(pad_hyper)

    new_cube = deque()
    for hyper in cube:
        nh = []
        for dimension in hyper:
            nd = []
            for i in range(len(dimension)):
                nd.append([status for status in dimension[i]])
            nh.append(nd)
        new_cube.append(nh)

    # 변환 코드
    for w in range(len(cube)):
        for z in range(len(cube[0])):
            for y in range(len(cube[0][0])):
                for x in range(len(cube[0][0][0])):
                    change_status(cube,new_cube,x,y,z,w)
                new_cube[w][z][y] = ''.join(new_cube[w][z][y])


    cube = new_cube

    # # 출력 코드
    # mid_w = len(cube) // 2
    # mid_z = len(cube[0]) // 2
    # print(mid_w, mid_z)
    # print(len(cube), len(cube[0]))
    # for w in range(len(cube)):
    #     for z in range(len(cube[0])):
    #         print(f'z={z - mid_z}, w={w - mid_w}')  # 차원 높이
    #         for row in cube[w][z]:
    #             print(row)
    #         print('')



count = 0
for w in range(len(cube)):
    for z in range(len(cube[0])):
        for y in range(len(cube[0][0])):
            for x in range(len(cube[0][0][0])):
                if cube[w][z][y][x] == '#':
                    count+=1

print(count)


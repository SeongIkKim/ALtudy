with open('inputs.txt') as f:
    S = f.read().strip().split('\n')

direction = {0:'N', 90:'E', 180:'S', 270:'W'}
direction.update({v:k for k,v in direction.items()}) # k, v 뒤집기
f = 90
d = {'E':0, 'W':0, 'N':0, 'S':0}

wp = {'E':10, 'W':0, 'N':1, 'S':0}

for line in S:
    i,val = line[0], int(line[1:])
    # print(i, val)
    if i == 'F':
        for key in wp.keys():
            d[key] += wp[key]*val
    elif i in d.keys():
        wp[i] += val
    elif i == 'L':
        new_wp = dict()
        for key in wp.keys():
            ab = direction[key]-val # 각도계산
            ab = 360+ab if ab<0 else ab # 계산각도 변환
            new_wp[direction[ab]] = wp[key] # 옮겨적어놓기
        wp = new_wp
    elif i == 'R':
        new_wp = dict()
        for key in wp.keys():
            ab = (direction[key]+val)%360
            new_wp[direction[ab]] = wp[key]
        wp = new_wp
    # print('wp ',wp)
    # print('d ', d)

answer = (abs(d['E']-d['W'])) + (abs(d['N']-d['S']))
print(answer)

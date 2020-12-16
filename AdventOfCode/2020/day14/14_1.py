from collections import defaultdict

with open('inputs.txt') as f:
    sets = f.read().strip().split('ma')[1:]

mem_d = defaultdict(int)


for set in sets:
    lines = set.strip().split('\n')

    mask = lines[0].split(' = ')[1]

    mems = []

    for line in lines[1:]:
        line = line.replace('mem[', '').replace('] =','')
        i,v = map(int, line.split())
        mems.append((i,f'{v:036b}'))


    # i = 메모리 인덱스
    # v = 해당 메모리에 덮어쓸 값
    for i,v in mems:
        for index in range(len(v)):
            if mask[index] == 'X':
                continue
            else:
                v = ''.join([v[:index],mask[index],v[index+1:]])
        # 저장할땐 int로
        mem_d[i] = int(v, 2)

# print(mem_d)
print(sum(mem_d.values()))


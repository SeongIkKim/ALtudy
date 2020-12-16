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
        mems.append((f'{i:036b}',v))
    # --- mems에는 (string i 이진수, int v) --


    # i = 비트마스크를 씌울 메모리 인덱스 이진수
    # v = 해당 메모리에 덮어쓸 값
    for i,v in mems:
        s_list = ['']
        for index in range(len(i)):
            new_s_list = []
            if mask[index] == '0':
                for s in s_list:
                    new_s_list.append(''.join([s,i[index]]))
            elif mask[index] == '1':
                for s in s_list:
                    new_s_list.append(''.join([s,'1']))
            else :
                for s in s_list:
                    new_s_list.append(''.join([s, '0']))
                    new_s_list.append(''.join([s, '1']))
            s_list = new_s_list
        address_list = [int(s,2) for s in s_list]

        for address in address_list:
            mem_d[address] = v

print(mem_d)
print(sum(mem_d.values()))

'''
dp문제다.
메모리를 필요이상으로 많이 쓴거같긴한데..
'''

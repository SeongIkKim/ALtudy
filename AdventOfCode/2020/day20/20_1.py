from collections import defaultdict
import numpy

with open('inputs.txt') as f:
    tiles = [tt.split(':\n') for tt in f.read().strip().split('\n\n')]

T = dict()
for tile in tiles:
    T[int(tile[0][-4:])] = tile[1].split('\n')

M = defaultdict(dict)


# while any M.value has right l,r,u,d
# while True:
# for one in T.keys():
    # for the_other in [i for i in T.keys() if i != one]:
for one in [2311]:
    for the_other in [3079]:
        print(one, the_other)
        # up
        if 'u' not in M[one].keys() and T[one][0] == T[the_other][-1]:
            M[one]['d'] = the_other
            M[the_other]['u'] = one
        # down
        if 'd' not in M[one].keys() and T[one][-1] == T[the_other][0]:
            M[one]['u'] = the_other
            M[the_other]['d'] = one
        # right
        if 'r' not in M[one].keys() :
            a = ''.join([line[-1] for line in T[one]])
            b = ''.join([line[0] for line in T[the_other]])
            if a == b:
                M[one]['r'] = the_other
                M[the_other]['l'] = one
        # left
        if 'l' not in M[one].keys() and ''.join([line[0] for line in T[one]]) == ''.join([line[-1] for line in T[the_other]]):
            M[one]['l'] = the_other
            M[the_other]['r'] = one

for k,v in M.items():
    print(k, v)

'''
힘을 키워서 다시 도전한다..
부들부들..
'''

from collections import defaultdict

with open('inputs.txt') as f:
    foods = f.read().strip().split('\n')

igs_D = dict()
als_D = defaultdict(set)

all_igs_list = []
all_igs = set()

for food in foods:
    igs, als = food.split('(contains')
    igs = igs.strip().split()
    als = [i.strip() for i in als[:-1].strip().split(',')]
    # print(igs, als)
    all_igs_list.extend(igs)
    all_igs = all_igs.union(set(igs))
    for al in als :
        if not als_D[al]:
            als_D[al] = set(igs)
        als_D[al] = als_D[al].intersection(set(igs))

# print(als_D)
# print(all_igs)

while als_D:
    remove_list = []
    for al,igs in als_D.items():
        # print(al, igs, len(igs))
        if len(igs) == 1:
            igs_D[igs.pop()] = al
            remove_list.append(al)
        else:
            als_D[al] = [ig for ig in igs if ig not in igs_D.keys()]
            # print(als_D[al])
    # print(remove_list)
    for el in remove_list:
        del als_D[el]

# print(igs_D)

dummies = all_igs.difference(set(igs_D.keys()))

count =0
for i in all_igs_list:
    if i in dummies:
        count +=1

print(count)

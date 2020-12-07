    # if len(list(words)) > 10:
    #     outer = f'{words[0]} {words[1]}'
    #     inner = [f'{words[5]} {words[6]}', f'{words[9]} {words[10]}']
    #     for i in inner:
    #         rules_d[i].add(outer)
    # else:
    #     outer = f'{words[0]} {words[1]}'
    #     if words[4] != 'no':
    #         rules_d[f'{words[5]} {words[6]}'].add(outer) # 체크
    #         # inner = [f'{words[5]} {words[6]}'] # 이거써야되는거 아닌지 체크

outers= set()

for k, v in rules_d.items():
    print(k, v)

def search(d, target, outers):
    # print(target, ' can be in...')
    for i in d[target]:
        # print(i)
        search(d,i,outers)
        outers.add(i)

search(rules_d, 'shiny gold', outers)

print(outers)



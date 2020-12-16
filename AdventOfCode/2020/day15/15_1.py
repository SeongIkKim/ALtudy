with open('inputs.txt') as f:
    arr = [int(num) for num in f.read().strip().split(',')]


last_index = dict()
for i, v in enumerate(arr[:-1]):
    last_index[v] = i

last = arr[-1]

for i in range(len(arr), 2020):
    new = 0
    if last in last_index:
        new = (i-1) - last_index[last] # difference
    last_index[last] = i-1 # 갱신
    last = new # difference를 해당 턴에 speak. 즉 다음 턴의 last는 new

answer = last

print(last)

'''
어려운 코드도 아닌데 왜 못풀었을까..?
다 생각했던 내용인데.. 인덱스 정리가 안된다.
'''

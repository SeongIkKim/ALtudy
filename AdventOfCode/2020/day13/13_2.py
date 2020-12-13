from itertools import count

with open('inputs.txt') as f:
    t, ids = f.read().strip().split('\n')
    ids = [(x,int(y)) for x,y in enumerate(ids.split(',')) if y != 'x']

print(ids)


t = ids[0][1] # 최초의 time stamp
step = 1 # jump할 간격
for i, b in ids:
    # 문제 그대로 옮겼다. n에서 시작해서 step씩 건너뛰어가며 해당 시각(c) + index가 bus 간격으로 나뉘어 떨어지는지 검사한다.
    # bus 간격으로 나누어 떨어진다는 것은 해당 시각에 정확히 그 bus가 출발한다는 뜻.
    t = next(c for c in count(t, step) if (c + i) % b == 0)
    # bus가 출발하는 시각을 찾으면, 다음부터는 해당 bus간격까지 고려하여 step하도록 step을 누적하여 곱한다.
    # step을 그냥 b로 설정하는 것이 아니라 누적해서 곱함으로써, 지금까지 검사한 버스 간격들을 모두 만족하는 t만 다음 t의 후보로 삼는다.
    step *= b

print(t)

'''
reddit에서 풀이를 참고했다.

수학문제다. chinese remainder problem이라고 하는데..
식은 생각해냈으나 이걸 코드로 옮길 방법이 생각나지 않았다. 그냥 연립방정식 때려박고싶었다.
for문이나 while문을 써서 지저분하게 처리하지 않고 itertools를 잘 쓴 예인듯하다.
itertools 쓰는 법 배워야겠다.
step *= b도 신기한 한 수. 모든 이전의 것을 만족하려면 누적해서 곱해야한다(독립 사건들을 모두 곱해준다)느낌인듯...
'''

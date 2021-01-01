import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = collections.Counter(nums)
        L = [(v,k) for k,v in C.items()]
        L.sort(reverse=True)
        L = [k for v,k in L[:k]]
        return L

'''
104ms(43.51%)
19MB(12.21%)
카운터, 튜플리스트화, 정렬을 모두 써서 느린거같긴한데 일단은 통과.
'''

# solution - 우선순위 큐

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        heap = []
        for key, value in freqs.items():
            heapq.heappush(heap, (-value, key))
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])
        return ans

'''
104ms(43.51%)
18.8MB(22.25%)
우선순위 큐 사용해도 비슷한듯
'''

# Solution 2 - pythonic

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common: k개만큼 최다빈도 원소를 반환
        # zip함수 : python3 이상에서 제너레이터를 리턴. 2개 이상 시퀀스에 대하여 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 반환.
        # 편하게 생각하면, 행렬에서 열단위로 묶어주는것처럼 작용. 또, enumerate는 인덱스 리스트와 원소 리스트를 zip한것과 같은 결과.
        # *(애스터리스크) : 시퀀스 언패킹 연산자. 튜플이나 리스트를 풀어헤쳐준다.
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

'''
92ms(94.26%) 오차범위.
18.6MB
1. Counter의 most_common함수는 지정갯수만큼 리턴도 가능하다
2. zip함수는 argument로 들어온 시퀀스들을 인덱스단위로 묶어준다
3. 시퀀스 언패킹 연습해볼것.
'''

'''
* : 그냥 사용되었을때는 언패킹(시퀀스 풀어헤치기,괄호 해제)이지만, 함수 argument로 들어갈 경우 패킹(여러 변수를 묶어 하나의 변수로 넘김)
** : 시퀀스 언패킹이 아니라 키/값 페어 언패킹.
딕셔너리 안에 다른 딕셔너리를 집어넣어 언패킹하여 합칠수도 있음.
'''

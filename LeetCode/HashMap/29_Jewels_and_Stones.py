import collections

# 1st try

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        J = collections.defaultdict(bool)
        for jewel in jewels:
            J[jewel] = True
        count = 0
        for stone in stones:
            if J[stone]:
                count+=1
        return count

'''
32ms(55.38%)
14.4MB(8.25%)
'''

# 1st solution - Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0
        for jewel in jewels:
            count += freq[jewel]
        return count

'''
32ms(55.38%)
13.9MB(97.59%)
Counter 사용해 stone을 딕셔너리에 집어넣는 과정을 생략함.
'''

# 2nd solution - pythonic

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
'''
32ms(55.38%)
13.9MB(97.59%)
s in jewels의 결과가 boolean으로 나오고, 리스트 컴프리헨션이므로,
sum은 True의 갯수를 합쳐서 반환한다. 
'''

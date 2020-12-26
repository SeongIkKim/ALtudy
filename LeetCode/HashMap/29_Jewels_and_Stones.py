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

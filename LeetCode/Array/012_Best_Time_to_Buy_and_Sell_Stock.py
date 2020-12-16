import sys
from typing import List

# 1st try

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0

        output = 0
        top = prices[-1]

        for price in prices[::-1]:
            # 고점 찾기
            if price > top:
                top = price
            # 차이가 가장 큰 값 찾기
            elif top - price > output:
                output = top - price

        return output

'''
시간대가 52ms(96%)~80ms(9.13%)로 들쭉날쭉..
15.1MB(17.87%)

20-30ms정도는 서버상태에 따른 오차인듯하다.
'''

# solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize  # 갱신되어야 하는 값이므로 어떤 수보다도 큰 수, sys.maxsize로 설정

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

'''
60ms(70.22%) ~ 92ms(4%), 일반적으로 60ms
15.1MB(17.87%)
전형적인 문제패턴.
1. min/max를 잘 사용하여 가독성을 높이자
2. 갱신용 값이 필요할 때는 sys.maxsize 등을 사용한다. None을 사용하면 비교시 에러가 날 수 있다.
'''

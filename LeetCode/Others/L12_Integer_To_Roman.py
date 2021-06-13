from collections import deque

# my solution

class Solution:
    def intToRoman(self, num: int) -> str:
        sub_dic = {4: 'IV', 9: 'IX',
              40: 'XL', 90: 'XC',
              400: 'CD', 900: 'CM'}
        dic = {1:'I', 5:'V', 10:'X', 50:'L',
              100:'C', 500:'D', 1000:'M'}
        answer = deque()
        for place, digit in enumerate(str(num)[::-1]):
            digit = int(digit)
            origin_digit = digit * (10**place)
            if digit in [4,9]:
                answer.appendleft(sub_dic[origin_digit])
            elif origin_digit in dic.keys():
                answer.appendleft(dic[origin_digit])
            else:
                dividend = origin_digit
                roman = ''
                for val in sorted(dic.keys(), reverse=True):
                    q, remainder = divmod(dividend, val)
                    if q != 0:
                        roman += (dic[val]*q)
                        dividend=remainder
                answer.appendleft(roman)
        return ''.join(answer)

"""
수학적이긴 한데 중복해서 나타내야하는 숫자(else문) 처리가 우아하지 않다.
64ms(21.94%)
14.2MB(82.63%)
"""

# Solution 1

def intToRoman(self, num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    answer = ""
    for r, v in zip(romans, values):
        q, num = divmod(num, v)
        answer += q * r  # 몫만큼 문자 반복
    return answer

"""
44ms(88.09%)
14.3MB(26.79%)

1. zip의 유용한 사용 (dic보다 적기가 쉽다)
2. 숫자를 거꾸로 하는것이 아니라 dic을 거꾸로하기
3. if elif else문을 divmod로 통일
"""

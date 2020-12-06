from typing import List


# 1st try

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse() # pythonic하다. 그러나 리스트에만 제공된다(문자열엔 사용불가)

'''
196ms(70.96%)
18.4MB(5.66%)
'''

# 2nd try

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(l):
            if i<l/2:
                temp = s[l-1-i]
                s[l-1-i] = s[i]
                s[i] = temp

'''
위와 동일
'''

# 1st book-solution

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left] # 2nd try와 개념은 같지만 가독성이 훨씬 좋다
            left += 1
            right -= 1
# 전형적인 투포인터 방식으로, pythonic하지 않다

'''
192ms(83.46%)
18.4MB(5.66%)
'''

# 2st book-solultion(not common)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[::] = s[::-1] # pythonic하다. 문자열에도 사용가능하다.
        # s = s[::-1] # 공간복잡도를 O(1)로 제한하지 않았으면 이것도 잘 동작한다.

'''
184ms(97.12%)
18.6MB(5.66%)
'''

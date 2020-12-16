# 1st try

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        now = deque()
        reverse = deque()
        if s:
            for i in range(len(s)):
                alphanumeric = s[i].upper()
                if 65 <= ord(alphanumeric) <= 90 or 48<= ord(alphanumeric) <= 57:
                    now.append(alphanumeric)
                    reverse.appendleft(alphanumeric)
            for i in range(len(now)):
                if now[i] != reverse[i]:
                    return False
        return True

'''
212ms(5.04%)
19.9MB(10.46%)
'''

# 2nd : 1-2.py

from collections import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

'''
36ms (95.24%)
19.3MB(10.46%)
'''

# 3nd : 1-3.py
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱

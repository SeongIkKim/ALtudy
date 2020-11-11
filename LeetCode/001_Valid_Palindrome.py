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

# 1st try

class Solution:
    def isValid(self, s: str) -> bool:
        correct = {'(' : ')', '[': ']', '{': '}'}
        stack = []
        for i in range(len(s)):
            if not stack or s[i] in ['{','[','(']:
                stack.append(s[i])
            else:
                try:
                    if correct[stack[-1]] == s[i]:
                        stack.pop()
                        continue
                    else:
                        return False
                except:
                    return False
        if stack:
            return False
        return True

'''
24ms(94.48%)
14.4MB(15.00%)
코드가 간단해야하는데 왜 그렇지 않을까?
'''

# Solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # 여는 괄호는 스택에 다 집어넣는다
            if char not in table:
                stack.append(char)
            # 닫는 괄호가 먼저 나왔거나, 괄호 짝이 안맞을경우 바로 끝낸다.
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0 # stack이 다 비었으면 True --> if else문 축약.

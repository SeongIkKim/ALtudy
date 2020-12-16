# 1st try
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        L = []
        D = dict()
        for i in range(len(s)):
            letter = s[i]
            # 중복이 아닐경우 그대로 더함
            if letter not in D.keys():
                D[letter] = i  # 해당 문자의 인덱스를 기록해둠
                L.append(letter)
                continue
            # 중복일 경우 사전순으로 체크하여 더 낮은것으로 채택
            if L > L[:D[letter]] + L[D[letter] + 1:] + [letter]:
                D[letter] = i

        ans = ''.join(L)
        return ans

'''
사전순이라는 것이 한 글자가 갱신될때마다 결정되는것이 아니라,
전체를 보고 결정해야하기때문에 기각.
ex) bcabc -> bca vs cab이기때문에 bca로 결정되지만, 최종 답은 abc이므로.
'''

# 1st Solution - 재귀

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)): # 중복을 제거한 s letter중에 사전순으로 순서가 빠른것부터 분리를 시도해낸다.
            suffix = s[s.index(char):] # suffix는 '접미사'로, char를 분리할 수 있는지 알아보기 위해 떼내는 스트링.
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            # 즉, suffix 내에 s의 모든 종류 문자가 다 들어가 있다는 뜻
            # 그러면 suffix 앞의 부분은 날려도 상관없다는 뜻이다.
            if set(s) == set(suffix):
                # 중복을 제거한(replace) suffix를 새로운 s로하여 재귀 시도.
                # replace하면서, 결국 가장 앞의 char만 남고 나머지 char는 다 제거한다.
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        # 재귀 끝부분에 s는 빈 문자열
        # 탈출 구문
        return ''

'''
52ms(14.97%)
14.4MB(10.33%)
재귀를 사용하여 접두사를 확정하고 분리해내기.
1. suffix를 잡는 방식 : 알파벳순으로 char의 index를 찾아내어서 좌우 분리
2. 좌를 삭제해도 되는지 체크하는 방식 (if set(s) == set(suffix))
3. 재귀호출 어렵다...
'''

# 2nd Solution - 스택

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # seen은 처리된 문자를 담아두어서 추후에 처리 여부를 확인할 때 사용한다.
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter(char) -= 1
            # 처리된 문자일경우 스킵
            # 즉, 중복문자인데 앞에 나와있는 같은 문자가 이미 있어서 이번 것은 제거해야할때
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            # 1. stack이 비어있지않고
            # 2. 현재 문자 char가 stack에 들어간 가장 최근문자보다 사전순으로 앞서고
            # 3. 가장 최근문자가 아직 뒤에 남았으면
            # 최근에 처리했던 문자를 seen(처리여부)에서 제거하고, 추후에 다시 처리하도록 한다(중복제거에서 도태)
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

'''
36ms(67.28%)
14.4MB(24.88%)
재귀 코드가 더 우아하고 간결하지만, 스택이 더 빠르다
1. while문의 세 조건을 잘보자. 사전순으로 처리하기 위해 char를 스택의 top과 비교하고,
char 뒷부분에 남아있으면 중복제거한 뒤 seen(처리여부, 즉 확정)에서도 제거한다.
2. 확정된 char이면 뒤의 것은 그냥 stack에 더하지 않음으로써 도태시킨다.
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 굳이 seen을 만들지 않았다. 어차피 python list는 in기능(검색)을 지원한다.
        counter, stack = collections.Counter(s), []

        for char in s:
            counter[char] -= 1
            # 원래는 stack에 없지만, python 리스트에는 in 기능이 있으므로 seen을 사용하지 않는다.
            # 즉, 이미 확정된 부분(stack)에 해당 char가 중복으로 있으면, 뒤의 것은 건너뛰는 것(도태)
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)

'''
stack에는 원래 검색연산이 없지만, python 리스트에는 있으므로 굳이 set을 쓰지 않아도 된다.
이 방법이 변수 사용을 줄이고 간결한, pythonic한 방법이라고 할 수 있다.
'''

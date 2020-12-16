'''
첫번째 시도
from itertools import combinations

def solution(number, k):
    number = [c for c in number]
    
    n = list(combinations(number,len(number)-k))
    num = max(n)
    
    return ''.join(num)

시간초과
'''
'''
두번째 시도
def solution(number, k):
    number = [c for c in number]

    stack = [number.pop(0)]
    while k > 0:
        if stack[-1] >= number[0]:
            stack.append(number.pop(0))
        elif stack[-1] < number[0]:
            while stack and stack[-1] < number[0]:
                stack.pop()
                k-=1
                if k == 0:
                    break;
            stack.append(number.pop(0))
    stack += number
    
    if 

    return ''.join(stack)
테스트케이스 12 런타임에러
반례 '7777777', 2
'''

# 다른사람의 풀이방식을 참고해 만든 코드
from collections import deque

def solution(number, k):
    number = [c for c in number]
    number = deque(number)

    stack = [number.popleft()]
    while k > 0 and number: # 더 뺄 수가 없거나 number를 다 순회할 때까지 반복
        if stack[-1] >= number[0]: # stack의 마지막자리수보다 작으면 그대로 집어넣는다 (앞자리수가 더 크므로 더 큰수)
            stack.append(number.popleft())
        elif stack[-1] < number[0]: # stack의 마지막자리수보다 크면
            # stack의 수가 더 크도록 (앞자리 수가 더 커지도록) 계속 stack의 원소를 빼낸다
            while stack and stack[-1] < number[0]:
                stack.pop()
                k-=1
                if k == 0:
                    break;
            stack.append(number.popleft())
    
    if k == 0:
        stack += number
    else:
        # number를 다 순회했지만 아직 뺄 숫자가 더 남았다면 작은 수들이 모인 뒷자리부터 없애준다
        stack = stack[:-k]

    return ''.join(stack)

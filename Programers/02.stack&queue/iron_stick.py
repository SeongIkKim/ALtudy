'''
30분
1.( : append하고 raser = 0 ------ 막대시작
2.) : 2-1. 그 이전이 (면 pop하고 raser=1, +len(stack) ------ 레이저로 자름
      2-2. 그 이전이 (가 아니면 pop하고 raser=0 그냥 +1 ------ 막대 끝
'''

def solution(arrangement):
    stack = 0
    raser = 0
    answer = 0
    
    for i in arrangement:
        if i == '(':
            stack -= 1 # append
            raser = 1 # 괄호가 열린상태
        else: # i == ')'
            if raser == 1: # ()
                stack += 1 # pop
                raser = 0 # 레이저를 쏘고 괄호가 닫힘
                answer += abs(stack) # 한번 자를때마다 레이저가 자를 막대갯수만큼 토막이 더 생김
            else: # ))
                stack += 1 # pop
                answer += 1 # 막대가 끝났으면 한개 추가
    return answer
'''
1. (가격,인덱스)스택을 만든다.
2. for문을 돌리면서 원소를 만났을 때 해당 원소의 가격이
-->2-1: stack보다 싼 것이 있으면, while문으로 더 비싼 stack의 원소를 모두 찾아서 그 차이만큼 해당 인덱스의 answer을 빼주고, remove한다
-->2-2: 싼것이 없으면, 스택에 (가격,인덱스)를 집어넣고, answer에 l-(i+1)를 넣는다.

def solution(p):
    answer = []
    stack = [] # 1. (가격,인덱스) 스택
    l = len(p)
    is_element_min = 1 # 해당 원소보다 싼 주식가격이 있어서 stack에서 pop했는지 확인하는 토글
    for i in range(l): # 2. for문을 돌리면서 해당원소를 만났을 때 가격이
        for j in range(len(stack)-1,-1,-1): 
            if stack[j][0] > p[i]: # 2-1. 더 싼 것이 있으면,
                answer[stack[j][1]] -= stack[j][0]-p[i] # 차이만큼 answer빼주기
                is_element_min = 0
                stack.pop(j)
        if is_element_min == 1:
            stack.append((p[i],i))
        answer.append(l-i-1)
        is_element_min = 1
    return answer

테스트케이스 통과 x, 효율성도 실패

입력 : [ 1, 2, 3, 2, 3, 1 ] 출력 : [ 5, 4, 1, 2, 1, 0 ]
입력 : [ 3, 1 ] 출력 : [ 1, 0 ]

확인해보니까 문제를 잘못 이해한듯
한번이라도 떨어지는 순간이 아니라
자신을 기준으로 하한가인 날들을 다 빼줘야한다.
‘’’

'''
i로 한번 돌면서
첫놈기준으로
더 큰놈 -> 앞에 넣고
더 작거나 같은놈 -> 뒤에넣고

하고나면
[우선순위 1위 인덱스,우선순위 2위 인덱스, 우선순위 3위 인덱스…]

find(locatioin)해서 인덱스+1

def solution(p, l):
    order = [0];
    for i in range(1,len(p)):
        j = 0
        while(j<len(order) and p[i]<=p[order[j]]):
            if p[i] == p[order[j]]:
                break;
            j+=1
        order.insert(j,i)
        print("order",order)
    
    answer = 0
    return answer

---> 실패.

def solution(p, l):
    stack = []
    order = []
    
    j = p[0]
    for i in range(len(p)):
        if j >= p[i]:
            stack.append(i)
            print(stack)
            i+=1
        else: # j < p[i]
            order.append([i])
            order.append(stack)
            print("order추가",order)
            stack = []
            j = p[i]
            i+=1
    order.append(stack)
    print(order)
    answer = 0
    return answer

queue를 왜 사용해야하는지 이제 알았는데… 어떤 방식으로 사용해야할지 감이안온다.

문제는 쉬운데 왜 내가 핵심을 계속 못짚는 느낌이지? 
'''


# 참고할만한 풀이
def solution(p, l):
    answer=0
    while len(p) != 0:
        i=0
        # 가장 앞에있는 문서가 중요도가 가장 높은 경우
        if p[0] == max(p):
            p.pop(0) # 바로 빼낸다
            answer+=1 # 문서 한개를 먼저 빼냈으므로 answer(순서)를 한칸 밀어준다
            if l !=0: 
                l -= 1 # index가 한칸 줄어들었으므로 l도 한칸 빼준다
            else:
                return answer # 현재 location과 같으면(== 찾던 location에 도달했으면) answer을 반환한다
        
        # 가장 앞에 있는 문서가 중요도가 가장 높지 않은 경우
        else: 
            p.append(p.pop(0)) # 더 높은 우선순위문서가 있으면 일단 큐의 가장 뒤쪽에 붙는다
            if l == 0:
                l = len(p)-1 # 첫번째 문서의 순위를 알고싶었는데 가장 뒤쪽으로 밀렸으니 가장 뒤쪽 인덱스를 넣어준다.
            else :
                l -= 1 # 차례가 돌아올 때까지 l을 계속 빼준다
            
    return answer
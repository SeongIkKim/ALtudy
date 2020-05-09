'''
최초시도

from collections import deque

def bfs(graph,target,queue,depth):
    print(depth,":",queue)
    next_queue = deque() # 다음 depth의 큐
    
    while(queue): # 저번 depth에서 만들어진 queue, 즉 이번 level의 노드들을 모두 검사
        temp_word = queue.popleft()
        if temp_word == target: # 같으면 해당 level(depth), 즉 걸린 단계 수를 반환
            return depth
        else : # 다르면 일단 next_queue에 차곡차곡 집어넣는다
            next_queue.extend(graph[temp_word])
    
    return bfs(graph,target,next_queue,depth+1)
        

def solution(begin, target, words):
    if target not in words:
        return 0
    
    graph = {}
    
    for word in words :
        # 1개만 다른 단어는 다른 단어가 하나 뿐이므로 set으로 union시에 length가 3 + 1 = 4
        graph[word] = [i for i in words if len(set(word).union(set(i))) == 4] 
    
    first_queue = deque([i for i in words if len(set(begin).union(set(i)))==4])
    
    answer = bfs(graph,target,first_queue,1)
    
    return answer

test case
begin = "hit"
target = "hhh"
words = ["hhh","hht"]
실패.

set시에 만약 단어내에 같은 글자가 있으면 4보다 줄어들수도 있다는 것을 간과했다.
'''

# 내가 만든 코드
from collections import deque

def bfs(graph,target,queue,depth):
    next_queue = deque() # 다음 depth의 큐
    
    while(queue): # 저번 depth에서 만들어진 queue, 즉 이번 level의 노드들을 모두 검사
        temp_word = queue.popleft()
        if temp_word == target: # 같으면 해당 level(depth), 즉 걸린 단계 수를 반환
            return depth
        else : # 다르면 일단 next_queue에 차곡차곡 집어넣는다
            next_queue.extend(graph[temp_word])
    
    return bfs(graph,target,next_queue,depth+1) # 꼬리재귀 사용해 보았습니다.
        

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.insert(0,begin)
    
    graph = {}
    
    for one in words:
        adj = []
        for another in words:
            dif = 0
            for i in range(len(one)):
                if one[i] != another[i] :
                    dif +=1
                    if dif == 2: # 불필요한 연산을 줄이기 위해 2이상 차이나면 for문 탈출
                        break;
            if dif == 1:
                adj.append(another)
        graph[one] = adj
            
    
    first_queue = deque(graph[begin])
    
    answer = bfs(graph,target,first_queue,1)
    
    return answer
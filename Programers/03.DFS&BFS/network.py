'''
최초시도

def dfs(answer,n,computers,stack,com,k):
    if k == n :
        return
    
    for i in range(k,n):
        if computers[com][i] == 1:
            stack.append(i)
    print(stack)
    
    while stack :
        answer -= answer
        next_com = stack.pop()
        answer = dfs(answer,n,computers,stack,next_com,next_com+1)
        
        
    return answer
                

def solution(n, computers):
    
    stack = []
    answer = dfs(n,n,computers,stack,0,1)            
    
    return answer

dfs base code를 잘 기억해두자.
'''

# 참고할만한 코드

def dfs(graph, start_node):
    visit = list()
    stack = list()
    
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            
def solution(n, computers):
    for i in range(n):
        computers[i][i] = 0
    
    graph = {}
    
    for i in range(n):
        link = [j for j in range(n) if computers[i][j] == 1]
        graph[i] = link
    
    paths = map(sorted, [dfs(graph,node) for node in graph])
    
    answer = len(set("".join(map(str,path)) for path in paths))
    
    return answer


def dfs(graph,start_node,visited):
    visited[start_node] = True # 방문 표시

    print(graph[start_node])

    for node in graph[start_node]:
        if not visited[node]:
            visited[node] = True;
            visited = dfs(graph,node,visited)

    return visited


# 종만북 보고 만든 내 코드
def solution(n, computers):
    answer = 0

    for i in range(n):
        computers[i][i] =0

    graph = {}
    visited= {}

    for i in range(n):
        # 인접리스트 그래프 구성
        adj_list = [j for j in range(n) if computers[i][j] == 1]
        graph[i] = adj_list
        # 노드방문여부 초기화
        visited[i] = False


    for i in range(n):
        if not visited[i]:
            visited = dfs(graph,i,visited)
            answer += 1 #dfs가 호출되었으면, 지금까지의 network와 연결되지 않은 node란 뜻이므로 새 네트워크로 갯수를 추가한다.


    return answer
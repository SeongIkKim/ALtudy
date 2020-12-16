'''
def dfs(length,graph,visited,start,path):
    path.append(start)
    if len(path) == length+1:
        return path
    
    for goal in graph[start]:
        if not visited[(start,goal)]:
            visited[(start,goal)] = True
            path = dfs(length,graph,visited,goal,path)
        
    return path
    

def solution(tickets):
    length = len(tickets)
    graph = {}
    visited = {}
    
    for ticket in tickets:
        if ticket[0] not in graph.keys():
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
        visited[(ticket[0],ticket[1])] = False
    
    path = []
            
    return dfs(length,graph,visited,"ICN",path)

첫번째 시도. 재귀 호출은 잘 되나 런타임에러.
알고보니 같은 티켓이 있는 경우를 안빼준거였다.
'''

'''
백트래킹을 사용할 줄 몰라 tickets를 pop했는데도 문제가 해결되지않았다.
막다른 공항으로 다다랐을때는 다시 재귀를 취소하고 뒤로 돌아와야한다.

def dfs(length,graph,tickets,start,path):
    path.append(start)
    if not tickets:
        return path
    
    for goal in graph[start]:
        if [start,goal] in tickets:
            tickets.remove([start,goal])
            path = dfs(length,graph,tickets,goal,path)
    return path
    

def solution(tickets):
    length = len(tickets)
    graph = {}
    
    for ticket in tickets:
        if ticket[0] not in graph.keys():
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
    
    path = dfs(length,graph,tickets,"ICN",[])
    print(path)
    return path

 ex) 테스트케이스 예시

       티켓 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]

       return : ["ICN", "COO", "ICN", "BOO", "DOO"]
'''

# 참고할만한 코드
def dfs(graph,length,path,here):
    path.append(here)
    if len(path) == length+1: # 모든 티켓을 다쓴 길이만큼 이동하면 종료
        return True
    
    if here not in graph.keys():
        # 티켓이 남았고 공항에 도착했는데 다른곳으로 나갈 티켓이 없으면 잘못들어왔다는 이야기
        # 따라서 이 공항으로 오면 안된다. 경로를 취소하고(pop) False를 반환해 이 길이 잘못되었다는 것을 알려준다.
        path.pop()
        return False
    
    # 이 공항에서 갈 수 있는 공항 갯수만큼 다 시도해본다.
    for i in range(len(graph[here])):
        # backtracking 개념
        # 티켓을 사용하였으나(pop) 혹시 다시 돌아와야 하면 티켓사용을 취소(insert)할 것이다
        # there은 마지막으로사용한 티켓을 빼돌려두는 변수이다
        there = graph[here].pop()
        
        # 만약 갔는데 올바른 경로라면 True를 전달해 쭉 재귀문을 탈출한다
        if dfs(graph,length, path, there):
            return True
        # 갔는데 올바른 경로가 아니라면 다시 돌아와 티켓사용을 취소하고 빼돌려둔 티켓을 다시 추가시킨다.
        graph[here].insert(0, there)
    
    # 이 공항에서 갈수 있는곳을 다 가봤는데 다 막다른길이 나온다면 잘못들어왔다는 이야기
    # 따라서 이 공항으로 온 것을 취소하고 다시 원래 있던 곳으로 돌아간다.
    path.pop()
    return False
    

def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  
    
    for r in routes.keys():
        routes[r].sort(reverse=True)
    
    N = len(tickets)
    path = []
    
    if dfs(routes, N, path, "ICN"):
        answer = path            
        
    return answer
'''
1.루트노드에 0을 넣어놓은 뒤(계산에 영향이 안가도록), 리스트의 원소 계산을 +로 할지 -로 할지에 따라 2분기되는 이진트리로 구상한다.
2.하나의 원소는 하나의 level에 대응하므로, DFS로 탐색을 진행한다.
3.만약 리프노드에 도달했다면, 루트노드로부터 거쳐온 경로의 계산값을 타겟넘버와 비교하고 같다면 count를 올린다.
''' 

def dfs(visited,x,n,i,t,answer):
    if len(visited) == len(n)-1:
        if sum(visited) == t:
            return answer+1
    visited.append(x)
    answer = dfs(visited,n[i],n,i+1,t,answer)
    answer = dfs(visited,-n[i],n,i+1,t,answer)
    
    return answer

        
def solution(n, t):
    answer = 0
    visited = []
    answer = dfs(visited,0,n,0,t,answer)
    
    return answer
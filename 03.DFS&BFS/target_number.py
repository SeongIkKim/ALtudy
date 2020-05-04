'''
1.루트노드에 0을 넣어놓은 뒤(계산에 영향이 안가도록), 리스트의 원소 계산을 +로 할지 -로 할지에 따라 2분기되는 이진트리로 구상한다.
2.하나의 원소는 하나의 level에 대응하므로, DFS로 탐색을 진행한다.
3.만약 리프노드에 도달했다면, 루트노드로부터 거쳐온 경로의 계산값을 타겟넘버와 비교하고 같다면 count를 올린다.
'''    

def solution(n, t):
    answer = 0
    visited = []
    to_visit = [0] # 루트노드 0
    
    end = len(n)-1
    i=0
    while to_visit:
        now = to_visit.pop() # 현재 방문노드
        if now not in visited:
            visited.append(now)
            to_visit.extend([n[i],-n[i]])
            i+=1;
        if i == end:
            answer.append(sum[visited])
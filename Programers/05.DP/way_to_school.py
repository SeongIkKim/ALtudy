'''
첫 시도 

def solution(m, n, puddles):
    end = [m,n]
    points = [[1,1]]
    while end not in points:
        new_points = []
        for point in points:
            if [point[0]+1,point[1]] not in puddles and point[0] != m:
                new_points.append([point[0]+1,point[1]])
            if [point[0],point[1]+1] not in puddles and point[1] != n:
                new_points.append([point[0],point[1]+1])
        points = new_points
    
    return points.count(end)

시간 복잡도 초과.
'''

'''
두번째 시도

def solution(m, n, puddles):
    end = [m,n]
    points = [[1,1]]
    for i in range(m+n-2):
        new_points = []
        for point in points:
            if [point[0]+1,point[1]] not in puddles and point[0] != m:
                new_points.append([point[0]+1,point[1]])
            if [point[0],point[1]+1] not in puddles and point[1] != n:
                new_points.append([point[0],point[1]+1])
        points = new_points
        print(points)
    return points.count(end)
8번 시간복잡도 초과,
효율성 테스트 실패.
'''

# 참고할 만한 풀이
def solution(m, n, puddles):
    path = [[0 for i in range(n+1)] for j in range(m+1)] # 더미를 포함한 격자생성
    path[1][1] = 1 # 최초의 경우의 수 1
    
    for i in range(1,m+1): # 1부터 x좌표 m까지
        for j in range(1,n+1): # 1부터 y좌표 n까지
            if i == j == 1: # 최초의 경우의 수는 이미 1로 초기화 되었으니 패스
                continue;
            if [i,j] in puddles: # 만약 해당 좌표값에 웅덩이가 있다면
                path[i][j] = 0 # 해당 좌표로 갈 수 없으므로 path 갯수는 0이 된다
            else: # 그렇지않으면 왼쪽 격자 경우의 수와 위 격자 경우의 수를 합쳐 이번 격자의 경우의 수를 만들어준다
                path[i][j] = path[i-1][j] + path[i][j-1]
    
    return path[-1][-1]%1000000007

'''
i와 j값을 문제 조건 m,n 격자와 맞춰주기 위하여 [0,0],[0,1],[1,0]... 등의 더미 path를 만들어둔다(값은 0)
최초의 path, path[1][1]은 1가지 방법이고, path[i][j] = 왼쪽격자(path[i-1][j]) + 오른쪽격자(path[i][j-1])이다.
1,1을 0으로 바꿔버리는 경우의 수를 continue문으로 제외시키고,
만약 i,j가 웅덩이가 있는 격자라면 해당 격자로는 이동할 수 없으므로 path 수는 무조건 0이 된다.
결과적으로 마지막 격자에 이르는 경우의 수를 구해서 리턴.
'''

'''
dp를 수행할 때, 반복수행을 줄여야하는건 알겠는데, 어떤 값을 저장해서 다음 계산에 쓸것인지 감이 잘 안잡힌다.
항상 다음 수는 이전에 구해둔 경우의 수를 조합하여 만들 수 있다는 것을 기억하자.
'''
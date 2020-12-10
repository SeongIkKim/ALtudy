'''
최초시도
import math
def solution(triangle):
    path_sum = [triangle[0][0]]
    for row in range(1, len(triangle)):
        row_sum = []
        print("row:", row)
        for column in range(math.floor(math.log(len(path_sum), 2)) + 1):
            row_sum.append(path_sum[column] + triangle[row][column])  # 왼쪽으로 내려가기
            print(path_sum[column], triangle[row][column])
            row_sum.append(path_sum[column] + triangle[row][column + 1])  # 오른쪽으로 내려가기
            print(path_sum[column], triangle[row][column + 1])
        path_sum = row_sum

    print(path_sum)

    return max(path_sum)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
for column 문에서 range설정이 헷갈린다.
'''

# 참고할만한 코드
def solution(t):
    for i in range(1,len(t)):  # 이후에 i-1 인덱스가 나오므로 outOfRange를 피하기 위해 1부터 시작해준다
        for j in range(len(t[i])): # 각 레벨에 존재하는 원소에 대해서
            if j == 0: # 왼쪽 모서리 조건 - 이전 레벨의 가장 왼쪽 sum에만 계산해준다
                t[i][j] += t[i-1][0]
            elif j == len(t[i])-1: # 오른쪽 모서리 조건 - 이전 레벨의 가장 오른쪽 sum에만 계산해준다
                t[i][j] += t[i-1][-1]
            else: # 모서리가 아닌 경우 - 이전 레벨까지의 경우의 수 중 지금의 숫자를 더했을 때 더 큰합이 나오도록 할당한다
                t[i][j] += max(t[i-1][j-1],t[i-1][j])

    return max(t[i]) # 마지막까지 업데이트된 경우 바닥 레벨의 가장 큰 수가 가장 큰 합이다.

'''
따로 path_sum을 만들지 않고 triangle 리스트 내부를 업데이트한다.
모서리가 아닌 경우에 각 레벨별로 더 큰 합을 더하면 왜 큰합이 나오는지를 이해한다.
'''
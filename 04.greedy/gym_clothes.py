# 내가만든 코드
def solution(n, lost, reserve):
    
    hasClothes = [1] * n;
    
    for i in range(n):
        if i+1 in reserve:
            hasClothes[i] +=1
        if i+1 in lost:
            hasClothes[i] -=1
    
    for i in range(n-1):
        if hasClothes[i] - hasClothes[i+1] == 2:
            hasClothes[i]-=1
            hasClothes[i+1]+=1
        elif hasClothes[i] - hasClothes[i+1] == -2:
            hasClothes[i]+=1
            hasClothes[i+1]-=1
    
    answer = 0
    for i in hasClothes:
        if i >= 1:
            answer+=1
    
    return answer

'''
for문과 if문이 너무 많이 들어가고 반복이 많기때문에,
코드를 줄일 수 있는 함수 사용을 고려해야겠다.
'''
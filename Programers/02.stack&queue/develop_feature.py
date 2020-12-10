'''
def solution(p, s):
    answer = []
    p=[40, 93, 30, 55, 60, 65]
    s=[60, 1, 30, 5 , 10, 7]
    
    d = []
    # 모든 기능이 배포될 때까지 반복
    while p :
        for i in range(len(p)-1,-1,-1):
            print("i:",i)
            p[i]+=s[i]
            if p[i] >= 100:
                d.append(i)
                p.pop(i)
                s.pop(i)
                seq = list(range(len(d)))
                print("p",p,"d",d,"seq",seq)
        if d and set(d) == set(seq):
            print("진입")
            answer.append(len(d))
            print("answer추가",answer)
            d=[]
        print("now p ",p)
    return answer

이렇게 했지만 실패하고 말았다.

이유는 문제를 잘못 이해했기 때문에.
미리 만들어진 기능이 배포가능하다는 문제의 조건을 말 그대로 코드로 옮겨야한다.
'''

# 참고한 코드
def solution(progresses, speeds):
    answer = []
    
    # 1. 모든 기능이 배포될 때까지 반복
    while progresses:
        
        # 1. 각 기능들의 그 날 진행률을 더해줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        # 2. 완성된 기능이 있으면 배포함
        cnt = 0
        # 진행 상황이 100 이상이면, 배포 가능함. 이 때, 배포할 때 progresses, speeds 모두 제거해야 함.
        while progresses and progresses[0] >= 100: #--->이부분이 포인트다. progress중 가장 앞에 있는 작업이 끝나야 배포할 수 있다.
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        # 3. 배포 개수가 1개라도 있으면, answer에 넣어줌
        if cnt > 0:
            answer.append(cnt)
            
    return answer
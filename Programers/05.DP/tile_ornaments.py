'''
n==1일떄 4
n==2일때 6
n==3일때 10
n>=4일때 fib(n)*3 + fib(n-1)*2 + fib(n-2)*2 + fib(n-3)*1
'''
'''
첫번째 푼 방식 - dp를 사용하지 않음
def solution(N):
    fib = [0,1,1]
    for i in range(3,81):
        fib.append(fib[i-1]+fib[i-2])
    
    if N>=4:
        answer = fib[N]*3 + (fib[N-1]+fib[N-2])*2 + fib[N-3]*1
    else:
        perimeter = [0,4,6,10]
        answer = perimeter[N]
    
    return answer
'''
# dp 개념 적용 - bottom up --> 80까지 미리 계산해두지 않고 n까지 한번만 계산한다.

def solution(N):
    fib = [0,1,1]
    perimeter = [0,4,6]
    
    if N>=3:
        for i in range(3,N+1):
            fib.append(fib[i-1]+fib[i-2])
            perimeter.append(fib[i]*2 + perimeter[i-1])
    
    
    return perimeter[N]
def solution(n, computers):
    answer = n
    
    net = []
    for i in range(n):
        net.append(0)
        for j in range(n):
            if i != j  and computers[i][j] == 1:
                net[i] += 1
                
    print(net)
    
    
    return answer
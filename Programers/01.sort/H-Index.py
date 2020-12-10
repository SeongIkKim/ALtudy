def solution(citations):
    citations.sort(reverse=True)
    length = len(citations) # 발표된 논문의 총 갯수
    
    h = 0
    i = 0
    while i<length:
        # (citation[i],i+1) (인용횟수,그 횟수 이상 인용된 논문 수)
        new_h = citations[i] if citations[i]<i+1 else i+1
        if new_h>h :
            h = new_h
        else:
            break;
        i+=1    
        
    return h
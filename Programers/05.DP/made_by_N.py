'''
첫시도
def solution(N, number):
    dic = {5:1}
    
    for count in range(2,9):
        keys = dic.keys()
        new_keys = []
        for key in keys:
            new_keys += [key+N,key*N,int(key/N),int(N/key),int(str(N)*count)]
            if 0 in new_keys:
                new_keys.remove(0)
        for new_key in new_keys:
            if new_key in keys and dic[new_key] < count:
                continue
            dic[new_key] = count
            
    answer = dic[number] if number in dic.keys() else -1
    
    return answer
테스트케이스 1,5,6,7 실패.
'''

'''
두번째시도

def solution(N, number):
    dic = {5:1}
    
    for count in range(2,9):
        keys = dic.keys()
        new_keys = []
        for key in keys:
            l = [key-N,N-key,int(key/N),int(N/key)]
            l = [i for i in l if i>0]
            new_keys += l
            new_keys += [key+N,key*N,int(str(N)*count)]
            
        for new_key in new_keys:
            if new_key in keys and dic[new_key] < count:
                continue
            dic[new_key] = count
    
    answer = dic[number] if number in dic.keys() else -1
    
    return answer
'''


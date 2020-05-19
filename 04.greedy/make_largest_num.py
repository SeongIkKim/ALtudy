'''
첫번째 시도
from itertools import combinations

def solution(number, k):
    number = [c for c in number]
    
    n = list(combinations(number,len(number)-k))
    n_list = []
    for i in n:
        n_list.append(int(''.join(i)))
                
    return str(max(n_list))

시간초과
'''
'''
최초시도
def solution(name):
    answer = []
    alphabet = [spelling for spelling in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    
    for spelling in name:
        i = alphabet.index(spelling)
        answer.append(26-i if i>13 else i)
    
    print(answer)
    answer = sum(answer)
    answer += len(name)-1
    
    return answer

왼쪽으로 이동하여 조작하는 경우의 수를 고려하지 못해 실패
'''
'''
2차시도
def greedy(graph,name,letter_index,alphabet,turn,answer):
    letter = name[letter_index]
    if letter == 'A':
        if turn == 0:
            여기서 미완성
    
    if letter_index != 0:
        answer.append(1)
    
    i = alphabet.index(letter)
    answer.append(26-i if i>13 else i)
    
    greedy(graph,name,graph[letter_index][1],alphabet,name_visited,answer)
    greedy(graph,name,graph[letter_index][0],alphabet,name_visited,answer)
    
    return
    

def solution(name):
    name_visited = [0]*len(name)
    answer = []
    alphabet = [spelling for spelling in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    
    graph = {}
    
    for i in range(len(name)):
        adj = []
        adj.append(i-1 if i>=1 else len(name)-1)
        adj.append(i+1 if i<len(name)-1 else 0)
        graph[i] = adj
    
    global turn = 0
    greedy(graph,name,0,alphabet,turn,answer)
    
    print(answer)
    answer = sum(answer)
    
    return answer
'''
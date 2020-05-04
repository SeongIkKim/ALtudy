'''
1.루트노드에 0을 넣어놓은 뒤(계산에 영향이 안가도록), 리스트의 원소 계산을 +로 할지 -로 할지에 따라 2분기되는 이진트리로 구상한다.
2.하나의 원소는 하나의 level에 대응하므로, DFS로 탐색을 진행한다.
3.만약 리프노드에 도달했다면, 루트노드로부터 거쳐온 경로의 계산값을 타겟넘버와 비교하고 같다면 count를 올린다.
''' 
'''
# 최초시도

def dfs(visited,x,n,i,t,answer):
    if len(visited) == len(n)-1:
        if sum(visited) == t:
            return answer+1
    visited.append(x)
    answer = dfs(visited,n[i],n,i+1,t,answer)
    answer = dfs(visited,-n[i],n,i+1,t,answer)
    
    return answer

        
def solution(n, t):
    answer = 0
    visited = []
    answer = dfs(visited,0,n,0,t,answer)
    
    return answer
'''

'''
# 두번째시도

def dfs(visited,x,n,i,t,answer):
    print(x,i,"n길이",len(n),"visited길이",len(visited),visited,answer)
    if len(visited) == len(n):
        if sum(visited) == t:
            print("####")
            answer +=1
        return answer
    visited.append(x)
    answer = dfs(visited,n[i],n,i+1,t,answer)
    answer = dfs(visited,-n[i],n,i+1,t,answer)
    
    return answer

        
def solution(n, t):
    n=[1,2,3]
    answer = 0
    visited = []
    answer = dfs(visited,n[0],n,0,t,answer)
    answer = dfs(visited,-n[0],n,0,t,answer)

    return answer


'''

'''
# 세번째 시도

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def MakeTree(parent,left,right,x,n,i):
    print("지금만들노드는",x)
    node = Node(x)
    if left==True:
        parent.left = node
    elif right==True:
        parent.right = node
    
    if i == len(n):
        return
    
    MakeTree(node,True,False,n[i],n,i+1)
    MakeTree(node,False,True,-n[i],n,i+1)
        
def solution(n, t):
    n=[1,2,3]
    answer = 0
    
    root = Node(0)
    MakeTree(root,True,False,n[0],n,1)
    MakeTree(root,False,True,-n[0],n,1)
    
    stack=[]
    count = 0
    while(count == 2**len(n)):
        node = root
        result = 0
        while(node->left == None or node->right == None):
            result += node.data
            node = node->left 
            아 left로 갈지 right로 가야할지 못정해주겠다.
        
        

    return answer

'''

'''
기억해 둘 부분
1. dfs라고 해서 무조건 한 라인을 쭉 타고 내려가서 result를 만들지 않아도 된다. 각 depth에 대하여 계산된 answer들을 리스트로 저장해두어도 된다.
2. 재귀나 stack을 이용하지 않아도 dfs를 계산할 수 있다.
'''

def solution(numbers, target):
    answer_list = [0]
    
    for i in numbers:
        temp_list = []
        for answer_until_now in answer_list: # 한 depth씩 내려갈때마다 각 line별로 계산된 answer들에 대하여
            temp_list.append(answer_until_now+i) # 더했을경우
            temp_list.append(answer_until_now-i) # 뺐을경우
            # 이 과정이 끝나면 temp_list에는 원래 answer_list에서 한 depth 더 내려가서, *2개의 answer들이 더 생겨있다.
        answer_list = temp_list
    
    answer = answer_list.count(target)
    return answer
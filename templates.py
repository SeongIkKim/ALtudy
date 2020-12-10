## Collections
'''
# defaultdict(factory함수)
해당 키가 없을시 factory 함수로 기본값을 생성하는 자료형 - dict의 set_default보다 빠름
'''

## Strings
'''
# 정규표현식
치환 - re.sub(<정규표현식(치환대상)>,<치환어(치환결과)>, <대상 string>)
'''

## 기타 패키지
'''
# sys
시스템 최소/최대값 설정 - sys.minsize, sys.maxsize
'''
## Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 리스트 뒤집기
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 리스트 합치며 정렬하기
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next,l2)
    return l1

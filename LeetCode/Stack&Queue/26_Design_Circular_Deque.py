# 1st try

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dq = [None] * k
        self.maxlen = k
        self.f = 0
        self.r = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.dq[self.f] is None:
            self.dq[self.f] = value
            self.f = (self.f - 1) % self.maxlen
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.dq[(self.r + 1) % self.maxlen] is None:
            self.r = (self.r + 1) % self.maxlen
            self.dq[self.r] = value
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.dq[(self.f + 1) % self.maxlen] is not None:
            self.f = (self.f + 1) % self.maxlen
            self.dq[self.f] = None
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.dq[self.r] is not None:
            self.dq[self.r] = None
            self.r = (self.r - 1) % self.maxlen
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.dq[(self.f + 1) % self.maxlen] is None else self.dq[(self.f + 1) % self.maxlen]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.dq[self.r] is None else self.dq[self.r]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.f == self.r and self.dq[self.f] is None else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.f == self.r and self.dq[self.f] is not None else False


# Solution - linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

'''
Deque 연산같이 리스트 앞에 요소를 추가하는 경우 O(n)이 되므로, 배열을 그대로 사용하는것은 좋지 않다.
연결 리스트를 사용하여 구현했다.
'''

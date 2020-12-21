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

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

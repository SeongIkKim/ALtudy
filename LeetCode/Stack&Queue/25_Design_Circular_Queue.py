# Solution

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.f = 0
        self.r = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.r] is None:
            self.q[self.r] = value
            self.r = (self.r + 1) % self.maxlen
            return True
        return False

    def deQueue(self) -> bool:
        if self.q[self.f] is None:
            return False
        self.q[self.f] = None
        self.f = (self.f + 1) % self.maxlen
        return True

    def Front(self) -> int:
        return -1 if self.q[self.f] is None else self.q[self.f]

    def Rear(self) -> int:
        # rear는 항상 삽입 후에 한칸 더 이동해 비어있는 칸을 가리키도록 설정되어있다
        return -1 if self.q[self.r - 1] is None else self.q[self.r - 1]

    def isEmpty(self) -> bool:
        return self.f == self.r and self.q[self.f] is None

    def isFull(self) -> bool:
        return self.f == self.r and self.q[self.f] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

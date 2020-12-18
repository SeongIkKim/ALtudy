#1st try

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while len(self.s) > 1:
            tmp.append(self.s.pop())
        result = self.s.pop()
        while tmp:
            self.s.append(tmp.pop())
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
32ms(45.40%)
14.3MB(19.14%)
pop은 O(n)이고 나머지는 다 O(1)
'''

# solution

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()  # input, output을 뒤집어서 기존의 front가 rear로 오게한다.
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output:
            # output이 비어있으면, input에서 차례로 pop해 모두 옮겨담는다(순서는 반대가 된다)
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]  # 기존의 input[0] = output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
24ms(93.05%)
14.3MB(19.14%)
굳이 임시 리스트에서 다시 원래 리스트로 돌리지 말고, 옮겨담으며 해결(peek)
peek와 pop은 O(n), 나머지는 O(1)
'''

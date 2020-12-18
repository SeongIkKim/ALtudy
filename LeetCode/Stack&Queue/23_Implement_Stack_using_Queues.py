# 1st try

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not len(self.q) else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
32ms(47.43%)
14.4MB(19.20%)
사실.. 뭘 어떻게 풀라는건지 감이 안온다.
차라리 C였으면 열심히 풀었을것같다.
'''

# solution

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

'''
28ms(77.56%)
14.4MB(19.20%)
popleft랑 append만 사용하라는 이야기였나보다.
push할 때만 O(n),나머지는 모두 O(1)이다.
'''

# Problem from LeetCode
# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        """
        Because we can only use stack functions to implement queue we will need 
        auxiliary stack to push items into the queue where back of the array will be our 
        front and vice versa. Just like towers of Hanoi problem :)
        """
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Step1: Move all elements from stack1 to stack2 one by one
        Step2: Add element to stack1
        Step3: Add elements from s2 back to s1 so we can access our front
        Done!!!
        Now just do other operations on stack1 very easily
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
     def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

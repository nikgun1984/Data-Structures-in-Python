# Stack implementation using LinkedList

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self,value):
        new_node = Node(value)
        if self.length==0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length+=1

    def pop(self):
        if self.top is None:
            return "None"
        if self.top == self.bottom:
            self.bottom = null
        self.top = self.top.next
        self.length-=1

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.length==0

    def print_list(self):
        node = self.top

        while node:
            print(node.value, end=',')
            node = node.next;
        print("\b")

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(9)
stack.print_list()
print()
stack.pop();
stack.print_list()
print(stack.peek())
print(stack.is_empty())



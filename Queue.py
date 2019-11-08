# I will be implementing Queue only using LinkedList due to time complexity
# for array is O(n)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self) -> int:
        return self.first.value

    def enqueue(self, value) -> 'None':
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self) -> int:
        if self.first is None:
            return None
        if self.first == self.last:
            return None
        else:
            self.first = self.first.next
        self.length -= 1
        return self.first.value

    def print_list(self) -> 'None':
        dummy = self.first
        while dummy:
            print(dummy.value, end=',')
            dummy = dummy.next
        print('\b')


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.print_list()
print()
val = queue.dequeue()
queue.print_list()
print(f'The first element that will be popped is {queue.peek()}')

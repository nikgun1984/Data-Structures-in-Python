class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def size_list(self) -> int:
        cur = self.head
        count=0
        while cur:
            cur = cur.next
            count+=count
        return count

    """
    Will add Node to the end of the list
    """
    def append(self,data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    """
    Will add Node to the beginning of the list
    """
    def prepend(self,data) -> None:
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self,data,node) -> None:

        if not node: # if node is not in the list
            print('Previous list is not in the list')
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def delete(self, data) -> None:
        cur_node = self.head
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None

        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_at_position(self,position) -> None:
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None

        count = 0
        prev = None
        while cur_node and count!=position:
            prev = cur_node
            cur_node = cur_node.next
            count+=1

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    """
    Will traverse through the list and print Node after Node
    """
    def print_list(self) -> None:
        dummy_node = self.head
        while dummy_node: #  OR is not None
            print(dummy_node.data)
            dummy_node = dummy_node.next


llist = LinkedList()
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(1)

llist.prepend(2)
llist.insert(5,llist.head.next)
llist.delete(8)     # 2,4,5,6,1
llist.delete_at_position(3)
llist.print_list()

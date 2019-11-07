class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def size_list(self) -> int:
        cur = self.head
        count = 0
        while cur:
            count+=1
            cur = cur.next
        return count

    def len_recursive(self,head) -> int:
        '''
        Recursive Method to get our length of the list
        '''
        if head is None:
            return 0
        return 1+self.len_recursive(head.next)

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
            print(dummy_node.data,end=',')
            dummy_node = dummy_node.next
    """
    Swap Nodes with data in the nodes
    """
    def swap_nodes(self,key_1,key_2) -> "None":
        if key_1==key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data!=key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data!=key_2:
            prev_2=curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next,curr_2.next = curr_2.next,curr_1.next


llist = LinkedList()
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(5)
llist.append(7)


llist.prepend(2)
llist.insert(5,llist.head.next)
print(f'Size before deletion is {llist.size_list()}')
llist.delete(8)     # 2,4,5,6,1
llist.delete_at_position(3)
print(f'Size after deletion is {llist.size_list()}')
print(f'Size after deletion is {llist.len_recursive(llist.head)}')

llist.print_list()

llist.swap_nodes(2,4)
print('After swapping: ')
llist.print_list()


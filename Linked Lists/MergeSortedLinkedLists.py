"""
LeetCode Easy Problem

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def merge_two_lists(self, l1: Node, l2: Node) -> Node:
        """
        Create dummy Node which will connect lists based on which value is
        smaller and then move list to its next node after completing connection
        1. Create dummy node and pointer to move it through both lists

        |l1|    1->3->5->9->None
        |l2|    2->4->8->None
        |dummy| 0->None
        |l3| holds memory of dummy node. we will use it to move through the lists

        2. Find the value which is smaller either in l1 or l2 and
        hold the memory of that smaller node in the l3.next

        3. Connect the rest of the remaining list to l3

        4. Return |dummy.next| because using just |dummy| will return 0
        """
        dummy = Node(0)
        l3 = dummy

        while l1 and l2:
            if l1.value <= l2.value:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2

        return dummy.next


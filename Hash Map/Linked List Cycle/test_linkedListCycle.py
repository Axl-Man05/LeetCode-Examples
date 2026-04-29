import unittest
import builtins
from typing import Optional

# Import the standalone ListNode class
from list_node import ListNode

# Inject Optional and ListNode into builtins so that linkedListCycle.py 
# can be imported without throwing NameError, keeping it 100% LeetCode copy-pasteable.
builtins.Optional = Optional
builtins.ListNode = ListNode

from linkedListCycle import Solution

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to create a cycle in a linked list
def create_cycle(head, pos):
    if pos == -1 or not head:
        return head
    
    cycle_node = None
    tail = head
    index = 0
    
    while tail.next:
        if index == pos:
            cycle_node = tail
        tail = tail.next
        index += 1
        
    # If the pos was the last node
    if index == pos:
        cycle_node = tail
        
    # Connect the tail to the cycle node
    tail.next = cycle_node
    return head

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_has_cycle_true(self):
        # Input: head = [3,2,0,-4], pos = 1
        head = create_linked_list([3, 2, 0, -4])
        head = create_cycle(head, 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_has_cycle_true_small(self):
        # Input: head = [1,2], pos = 0
        head = create_linked_list([1, 2])
        head = create_cycle(head, 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_has_cycle_false(self):
        # Input: head = [1], pos = -1
        head = create_linked_list([1])
        head = create_cycle(head, -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_empty_list(self):
        # Input: head = [], pos = -1
        head = create_linked_list([])
        head = create_cycle(head, -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_long_list_no_cycle(self):
        # Test a long list without a cycle
        head = create_linked_list(list(range(100)))
        self.assertFalse(self.solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main()

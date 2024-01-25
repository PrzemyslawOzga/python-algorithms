# Leetcode #2
# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked
# list. You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.
from typing import Optional


class ListNode:
    """
    Create Python linked-list.
    Information URL: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
    """

    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next_val = next_val


def add_two_numbers(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    
    dummy_node = current = ListNode(0)
    carry_value = 0
    while list1 or list2:
        first_value = list1.val if list1 else 0
        second_value = list2.val if list2 else 0
        total = first_value + second_value + carry_value
        current.next_val = ListNode(total % 10)
        carry_value = total // 10
        if list1:
            list1 = list1.next_val
        if list2:
            list2 = list2.next_val
        current = current.next_val
    if carry_value:
        current.next_val = ListNode(carry_value)
    return dummy_node.next_val

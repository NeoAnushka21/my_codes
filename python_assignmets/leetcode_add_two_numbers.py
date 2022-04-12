# Definition for singly-linked list.
import self as self


class ListNode:
    def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp01 = l1                  # temp variable for 1st list
        temp02 = l2                  # temp variable for 2nd list
        addition = ListNode()        # List to store sum
        temp03 = addition            # temp variable to loop through addition
        carry = 0

        while temp01 is not None or temp02 is not None:  # condition given to continue until both l1 and l2 become None
            x = temp01.val if temp01 is not None else 0  # storing value in x variable if val exists
            y = temp02.val if temp02 is not None else 0
            s = carry + x + y
            carry = s // 10
            temp03.next = ListNode(s % 10)  # storing the Units place of s in list
            temp03 = temp03.next

            if temp01 is not None:
                temp01 = temp01.next
            if temp02 is not None:
                temp02 = temp02.next

        if carry > 0:
            temp03.next = ListNode(carry)  # add the last node only if the carry over is 0 ie no carry

        return addition.next  # since head was dummy

obj = Solution()
print(obj.add_two_numbers([2,3,5],[1,3,4]))

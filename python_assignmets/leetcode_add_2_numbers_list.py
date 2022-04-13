class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Head of the new linked list - this is the head of the resultant list
    head = None
    # Reference  head which is null at this point
    temp = None
    # Carry
    carry = 0
    # Loop for the two lists
    while l1 is not None or l2 is not None:
        # Start of each iteration, adding carry from the last
        sum_value = carry
        # length of list may be unequal, we are checking if the
        # current node is null for one of the lists
        if l1 is not None:
            sum_value += l1.val
            l1 = l1.next
        if l2 is not None:
            sum_value += l2.val
            l2 = l2.next
        # Adding  total sum_value % 10 to the new node in new list
        node = ListNode(sum_value % 10)
        # Carry to add in the next iteration
        carry = sum_value // 10
        # If this is the first node/head
        if temp is None:
            temp = head = node
        # Other node
        else:
            temp.next = node
            temp = temp.next
    # check carry left for last iter
    # If left create new node
    if carry > 0:
        temp.next = ListNode(carry)
    return head


head1 = ListNode(2)
head1.next = ListNode(3)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

result = addTwoNumbers(head1, head2)
while result is not None:
    print(str(result.val),end=" ")
    result = result.next
# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a new list node to store the sum
        sum = ListNode(0)
        # Create a pointer to the sum list node
        p = sum
        # Create a carry variable to store the carry value
        carry = 0
        # Loop through the list nodes until both l1 and l2 are None
        while l1 or l2:
            # If l1 is not None, add the value to the sum
            if l1:
                carry += l1.val
                l1 = l1.next
            # If l2 is not None, add the value to the sum
            if l2:
                carry += l2.val
                l2 = l2.next
            # Create a new list node with the carry value
            p.next = ListNode(carry % 10)
            # Move the pointer to the next list node
            p = p.next
            # Update the carry value
            carry //= 10
        # If the carry value is not 0, add a new list node with the carry value
        if carry:
            p.next = ListNode(carry)
        # Return the sum list node
        return sum.next

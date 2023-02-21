# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a new linked list
        # create a carry variable
        # create a sum variable
        # create a while loop that runs while l1 or l2 is not None
        # create a sum variable that adds the values of l1 and l2
        # create a carry variable that adds the values of l1 and l2
        # if the sum is greater than 10, then set the carry to 1 and the sum to the remainder
        # if the sum is less than 10, then set the carry to 0 and the sum to the sum
        # create a new node with the sum value
        # set the next value of the new node to the next value of l1 and l2
        # return the new node
        new = ListNode()
        carry = 0
        sum = 0
        while l1 or l2:
            sum = l1.val + l2.val + carry
            if sum > 10:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
            new = ListNode(sum)
            new.next = l1.next
            new.next = l2.next
        return new

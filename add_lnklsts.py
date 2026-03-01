# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sums = []
        while l1 or l2 :
            if l1 and l2 :
                sum = l1.val + l2.val + carry
                carry = 0
                if sum >= 10:
                    carry = 1
                sums.append(sum%10)
                l1 , l2 = l1.next , l2.next
            elif l1 :
                sum = l1.val + carry
                carry = 0
                if sum >= 10:
                    carry = 1
                sums.append(sum%10)
                l1 = l1.next
            else:
                sum = l2.val + carry
                carry = 0
                if sum >= 10:
                    carry = 1
                sums.append(sum%10)
                l2 = l2.next
        if carry != 0 :
            sums.append(carry)

        ini = ListNode(0)
        current = ini
        for i in sums:
            current.next = ListNode(i)
            current = current.next 
        return ini.next

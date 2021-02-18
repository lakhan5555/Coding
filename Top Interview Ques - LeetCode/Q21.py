class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(-1)
        temp1 = temp
        while l1 and l2 :
            if l1.val <= l2.val:
                temp1.next = l1
                l1 = l1.next
            else:
                temp1.next = l2
                l2 = l2.next
            temp1 = temp1.next
        if l1 != None:
            temp1.next = l1
        else:
            temp1.next = l2
        return temp.next   

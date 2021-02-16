class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        prev = None
        Next = None
        while temp:
            Next = temp.next
            temp.next = prev
            prev = temp
            temp = Next
        return prev    
            
   

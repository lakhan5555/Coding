class Solution:
    def fn(self,n1,n2,headA,headB):
        d = n1-n2
        tempA = headA
        tempB = headB
        for i in range(d):
            tempA = tempA.next
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        return None    
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1 = headA
        temp2 = headB
        n1 = 0
        while temp1:
            n1 += 1
            temp1 = temp1.next
        n2 = 0
        while temp2:
            n2 += 1
            temp2 = temp2.next
        
        if n1 >= n2:
            return self.fn(n1,n2,headA,headB)
        else:
            return self.fn(n2,n1,headB,headA)
            
        

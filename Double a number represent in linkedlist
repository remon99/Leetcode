    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.f(head)
        if self.c==1:
            return ListNode(1,head)
        else:
            return head


        # Calculate the original value represented by the linked list
    def f(self,curr):
        if curr:
            self.f(curr.next)
            curr.val=curr.val*2 + self.c
            if(curr.val>9):
                curr.val%=10
                self.c=1
            else :
                self.c=0

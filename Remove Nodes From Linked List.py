# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        i=0
        itr=head
        while itr:
            #maxx=max(itr.val,maxx)
            if not l:
                l.append(itr.val)
            elif l[-1]<itr.val:
                while l and l[-1]<itr.val:
                    l.pop()
                l.append(itr.val)
            else:
                l.append(itr.val)
            itr=itr.next
            i+=1
        if(i==len(l)):
            return head
        else:
            #l.reverse()
            head = None  # Initialize head as None
            current = None

            for val in l:
                if head is None:
                    head = ListNode(val)
                    current = head
                else:
                    current.next = ListNode(val)
                    current = current.next

            return head

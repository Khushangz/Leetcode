# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        i=1
        while temp.next!=None:
            temp=temp.next
            i+=1
        if i==1:
            return None
        if n==1:
            temp=head
            i=1
            while temp.next.next!=None:
                temp=temp.next
            temp.next=temp.next.next
            return head

        n=i-n
        print(n)
        if n==0:
            head=head.next
            return head
        
        i=1
        temp=head
        while i<n:
            temp=temp.next
            i+=1
        print(temp.val)
        temp.next=temp.next.next
        return head
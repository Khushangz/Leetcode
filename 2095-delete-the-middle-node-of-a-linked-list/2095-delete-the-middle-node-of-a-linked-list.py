# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        j=0
        if not temp.next:
            head=None
            return head
        count=0
        mid=temp
        while temp.next!=None:
            temp=temp.next
            count+=1
            if count%2==1 and count>=3:
                mid=mid.next

        mid.next=mid.next.next
        return head


     
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node

    def pairSum(self, head: Optional[ListNode]) -> int:

                
        if head==None or head.next==None:
            return None
        count=0
        temp=head
        while temp.next!=None:
            count+=1
            temp=temp.next
        n=count
        count=0
        temp=head
        while count<n//2:
            temp=temp.next
            count+=1
        k=temp
        if n%2==0:
            temp=temp.next
        temp=temp.next
        start2=temp
        k.next=None
        node = None
        y=head
        while y:
            temp = y.next
            y.next = node
            node =y
            y = temp
        head=node
        sum=node.val+start2.val
        print(node.val,start2.val)
        temp=head
        while temp!=None and start2!=None:
            print(temp.val,start2.val)
            sum=max(temp.val+start2.val,sum)
            temp=temp.next
            start2=start2.next

        
        return sum



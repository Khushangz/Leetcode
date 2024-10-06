# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        if head==None or head.next==None:
            return head
        count=0
        temp=head
        while temp.next!=None:
            count+=1
            temp=temp.next
        print(count)
        p=temp
        head.val,temp.val=temp.val,head.val
        p=temp
        k=head.next
        x=1
        while x<=(count//2):
            temp=k
            while temp.next!=p:
                temp=temp.next
            temp.val,k.val=k.val,temp.val
            p=temp
            x+=1
            print(x)
            k=k.next
        return head
            

        
         
        
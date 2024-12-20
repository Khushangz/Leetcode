# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def loop(self,temp,arr):
        if temp==None:
            return
        if temp.left==None:
            if temp.right==None:
                arr.append(temp.val)
                return
        self.loop(temp.right,arr)
        self.loop(temp.left,arr)
            
        



        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr1=[]
        self.arr2=[]
        self.loop(root1,self.arr1)
        self.loop(root2,self.arr2)
        print(self.arr1,self.arr2)
        if self.arr1==self.arr2:
            return True
        else:
            return False
        
            
            

            



        
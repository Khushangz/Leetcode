# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def roots(self,que):
        level=[]
        q2=[]
        for i in que:
            if i.left:
                level.append(i.left)
                q2.append(i.left.val)
            if i.right:
                level.append(i.right)
                q2.append(i.right.val)
                
        return level,q2
                
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return([])
        que=[root]
        levels=[]
        out=[]
        levels.append([root.val])
        curr= root
        while que:
            que,q2=self.roots(que)
            if len(q2)==0:
                continue
            levels.append(q2)
        return levels
            
            
        
            
            
                
            
            
            
            
            
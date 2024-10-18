# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize result list and stack
        visited = []
        stack = []
        curr = root

        # Traverse the tree
        while curr or stack:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node
            curr = stack.pop()
            visited.append(curr.val)

            # Go to the right subtree
            curr = curr.right
        
        return visited

            
            
            
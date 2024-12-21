# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, current_max):
        if not node:
            return

        # If the current node's value is greater than or equal to the current maximum
        if node.val >= current_max:
            print(node.val)  # Debug print for the good node
            self.result.append(node)  # Add the good node to the result list
            current_max = node.val  # Update the current maximum

        # Traverse the left subtree with the updated maximum
        self.dfs(node.left, current_max)

        # Traverse the right subtree with the updated maximum
        self.dfs(node.right, current_max)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Initialize the result list to store good nodes
        self.result = []

        # Start DFS traversal with the root's value as the initial maximum
        self.dfs(root, root.val)

        # Debug print for all good nodes
        print("Good nodes:")
        for node in self.result:
            print(node.val)

        # Return the number of good nodes
        return len(self.result)

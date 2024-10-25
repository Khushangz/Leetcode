class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if not root:
            return []
        queue.append(root)

        def dfs(ans, queue):
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
# if queue empty, at bottom level, should not continue.
            if queue:
                dfs(ans, queue)
# post-order, such that we append from bottom to top.
            ans.append(temp)

        dfs(ans, queue) 
        return ans

        
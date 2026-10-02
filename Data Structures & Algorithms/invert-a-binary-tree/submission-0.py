# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        queue = deque([root]) #initialize and insert root node

        while queue: #while it's not empty
            node = queue.popleft() #remove the front node
            node.left, node.right = node.right, node.left
            if node.left: #if left child exists
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root






        
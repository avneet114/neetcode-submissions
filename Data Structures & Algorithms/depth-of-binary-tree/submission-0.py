# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Using UMPIRE Strategy:
Understand: 
Input: a root of a binary tree
Output: an integer which is the depth of the binary tree
Edge cases:
- binary tree is empty = return 0
- binary tree has just 1 root = return 1
constraints:
- the number of nodes in the tree are between 0 and 100
- the value of the nodes could be between -100 and +100

Match: Depth first search
Plan:
- check if root is empty -> return 0
- if root exists then recursively compute the depth of left subtree and right subtree 
- take the maximum of the two
- add 1 for the current node
depth of a tree = 1 + max dep of its left and right subtrees
Implement: check below
Review: since we traverse the entire treee
Time - O(n)
Space - O(n) - height of the tree (worst case) if not balanced  
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root: #if root exists
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, rightDepth) #+1 accounts for the current node


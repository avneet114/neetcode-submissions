# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understand:
To check whether one tree is a subtree of another, we do two things:

Walk through every node of the main tree (root) using DFS.
At each node, check if the subtree starting here is exactly the same as subRoot.
So for every node in the big tree:

If its value matches subRoot's root, we compare both subtrees fully.
If they are identical, subRoot is a subtree.
Otherwise, continue searching on the left and right children.
The helper sameTree simply checks whether two trees match exactly, node-for-node.
Match: DFS
Plan:
If subRoot is empty → return true (empty tree is always a subtree).
If root is empty but subRoot is not → return false.
At the current root node:
If sameTree(root, subRoot) is true, return true.
Recursively check:
isSubtree(root.left, subRoot)
isSubtree(root.right, subRoot)
Return true if either side returns true.
sameTree(root1, root2):

If both nodes are null → return true.
If only one is null → return false.
If values differ → return false.
Recursively check left children and right children.
Implement:
Review:
Evaluate:
Time - O(m * n), where m is the number of nodes in subRoot and n is the number of nodes in root
Space - O(m+n)
"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: #subtree is empty -> always a subtree
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False
        
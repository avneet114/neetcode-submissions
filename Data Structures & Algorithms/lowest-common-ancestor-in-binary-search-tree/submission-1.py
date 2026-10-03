# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understand: Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself.

Match: Iteration
Plan:
This is the iterative version of finding the Lowest Common Ancestor (LCA) in a Binary Search Tree (BST).
Because a BST is ordered:

Left subtree < node < right subtree
We can decide where both nodes lie just by comparing values.

If p and q are both greater than the current node -> move right.
If they are both smaller -> move left.
If they split (one on each side) or one equals the current node ->
current node is the LCA, because it's the first node where their paths diverge.
This avoids recursion and simply walks down the tree until the split point is found.
Evaluate:
Time - O(h), where h is the height of the tree
Space - O(1)
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root #curr is never null as p and q are guaranteed to be in bst

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


        
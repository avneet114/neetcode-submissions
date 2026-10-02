# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand:
two binary trees are the same if:
- their strucure is identical
- their corresponding nodes have the same values
so at every position:
- both nodes are null -> true
- if one is null but the other isn't -> false
- if both exist but values differ ->false
otherwise, compare their left subtrees and right subtrees recursively
Match: direct structural + value-based DFS comparison
Plan:
- if both p and q are null -> return true
- if only one is null, return false
- if their values differ, return false
then recursively compare:
p.left with q.left
p.right and q.right
- return true only if both subtree comparisons are true
Implement: see below
Review:
Evaluate: 
Time - O(n)
Space - O(h)
where n is the number of nodes in the tree and h in the height of the treee
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #both are null
            return True
        
        if p and q and p.val == q.val: #if they exist and their values are equal -> check their subtrees recursively
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False
            


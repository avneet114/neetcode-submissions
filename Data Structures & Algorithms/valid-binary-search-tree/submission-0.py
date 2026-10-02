# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand: given the root of a binary tree, return true if it's a valid binary search tree, otherwise return false
a valid binary search tree satisfies the following constraints
- everything on left subtree of a node is smaller than the node's value
- everything on the right subtree of a node is greater than the node's value
- both the left and right subtrees are also binary search trees
A Binary Search Tree isn’t just about each node being smaller or larger than its parent —
every node must fit within a valid value range decided by all its ancestors.
For the root, the allowed range is (-∞, +∞).
When you go left, the node’s value must be less than the parent, so the upper bound becomes smaller.
When you go right, the node’s value must be greater than the parent, so the lower bound becomes larger.
constraints
- number of nodes in the tree are betwene 1 and 10k
- no empty root
edge cases:
- one node, no children -> true
Match: BST, DFS
Plan:
- start DFS from the root with initial valid range (-infinity and +infinity)
- for each node:
- if node.val is not strictly between left,right then return false
recursively
- validate the left subtree with the updated range (left, node.val)
- validate the right subtree with the updated range (node.val, right)
Evaluate
Time: O(n)
Space: O(n)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
        

        
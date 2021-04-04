# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 6->2->4 root-> l -> r
class Solution:
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
         while root:
            if root.val > p.val and root.val >q.val:
                 #6(root) -> 2 -> 4 
                 # 2 should be LCA 
                 # Assign new root as root.left to return it (Cuz we gonna using a recursive)
                 root = root.left
            elif root.val < p.val and root.val <q.val:
                 # 6(root) -> 8  -> 9
                 # 8 should be CLA
                 # Assign new root as root.right to return it (Cuz we gonna using a recursive)
                root = root.right
            else:
                # 6(root) ->2 -> 8 (which is a binayry tree)
                return root



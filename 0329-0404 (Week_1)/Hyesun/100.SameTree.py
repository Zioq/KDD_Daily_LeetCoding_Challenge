# 100. Same Tree
# https://leetcode.com/problems/same-tree/
#explained on medium: https://anhyesun.medium.com/learning-python-with-interview-questions-3-80890131204f 
class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

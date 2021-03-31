/* 
AUTHOR: Jaeung Kim
DATE: 2021-03-29
TITLE: Daily Coding Challenge (KDD)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

*/

public class validateBST_210329 {

    
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) {this.val=val;}
        TreeNode(int val, TreeNode left, TreeNode right){
            this.val=val;
            this.left=left;
            this.right=right;
        }
    }
    class Solution {
        public boolean validate(TreeNode root, Integer low, Integer high) {
            
            if (root == null) {
                return true;
            }
            
            if ((low != null && root.val <= low) || (high != null && root.val >= high)) {
                return false;
            }
            
            return validate(root.right, root.val, high) && validate(root.left, low, root.val);
        }
    
        public boolean isValidBST(TreeNode root) {
            return validate(root, null, null);
        }
    }
}

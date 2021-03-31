public class l_235_lowest_common_ancestor_of_a_binary_search_tree {

  class TreeNode {
       int val;
       TreeNode left;
       TreeNode right;
       TreeNode(int x) { val = x; }
  }
 
     /**
      * optimized solution
      *
      * key: bst -> all right nodes are greater, all left nodes are smaller
      *      if p & q are not in the same side, common ancestor is the root node in the iteration
      */
     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
         int rootVal = root.val;
         int pVal = p.val;
         int qVal = q.val;
 
         if (pVal > rootVal && qVal > rootVal) {
             return lowestCommonAncestor(root.right, p, q);
         } else if (pVal < rootVal && qVal < rootVal) {
             return lowestCommonAncestor(root.left, p, q);
         }
         return root;
     }
 }
 
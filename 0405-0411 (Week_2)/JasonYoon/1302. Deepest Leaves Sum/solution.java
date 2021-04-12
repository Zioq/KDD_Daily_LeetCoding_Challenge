//Submission for 2021-04-11
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int deepestLeavesSum(TreeNode root) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        findDepth(root, 0, hash);
        return hash.get(hash.size()-1);
    }
    public void findDepth(TreeNode root, int depth, HashMap<Integer, Integer> hash){
        if(root == null)
            return ;
        int temp = 0;
        if(hash.containsKey(depth))
            temp = hash.get(depth);
        hash.put(depth, root.val+temp);
        findDepth(root.left, depth+1, hash);
        findDepth(root.right, depth+1, hash);
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class l_230_kth_smallest_element_in_a_bst {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    /**
     * first solution
     * not working
     */
    public int kthSmallestFirst(TreeNode root, int k) {
        List<Integer> al = new ArrayList<>();

        int[] arr = createArray(root, al);
        Arrays.sort(arr);
        return arr[k - 1];
    }


    public int[] createArray(TreeNode root, List<Integer> al) {
        if (root == null) return;
        al.add(root.val);
        createArray(root.left, al);
        createArray(root.right, al);

        return al.toArray();
    }

    /**
     * second solution
     * working, but slow
     */
    public int kthSmallestSecond(TreeNode root, int k) {
        List<Integer> al = new ArrayList<>();
        createList(root, al);
        Collections.sort(al);
        return al.get(k - 1);
    }

    public void createList(TreeNode root, List<Integer> al) {
        if (root == null) return;

        al.add(root.val);
        createList(root.left, al);
        createList(root.right, al);
    }

    /**
     * Optimized solution
     *
     * key: Inorder traversal returns elements in ascending order
     */
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> list = inOrder(root, new ArrayList<Integer>());
        return list.get(k - 1);
    }

    public List<Integer> inOrder(TreeNode root, List<Integer> list) {
        if (root == null) return list;

        inOrder(root.left, list);
        list.add(root.val);
        inOrder(root.right, list);

        return list;
    }
}

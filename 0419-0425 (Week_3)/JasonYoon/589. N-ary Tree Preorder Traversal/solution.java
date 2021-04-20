// Submission for 2021-04-20

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> list = new ArrayList<Integer>();
        Iterate(root, list);
        return list;
    }
    public void Iterate(Node root, List<Integer> list){
        if(root == null)
            return;
        list.add(root.val);
        for(int i = 0 ; i < root.children.size(); i++){
            if(root.children.get(i)==null)
                break;
            Iterate(root.children.get(i), list);
        }
    }
}

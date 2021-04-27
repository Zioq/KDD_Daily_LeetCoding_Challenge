// https://leetcode.com/problems/diameter-of-binary-tree/
// Monday Submission
var diameterOfBinaryTree = function(root) {
    let diameter = 0;
    const depthSearch = (root) => {
        if(!root) return 0;    

        const left = depthSearch(root.left);
        const right = depthSearch(root.right);

        diameter = Math.max(diameter, left+right);
        return Math.max(left, right) + 1;
    }
    depthSearch(root);
    return diameter;
};
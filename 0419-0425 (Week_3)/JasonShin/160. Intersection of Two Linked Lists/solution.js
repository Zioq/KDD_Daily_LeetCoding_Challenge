//https://leetcode.com/problems/intersection-of-two-linked-lists/
//Sunday submission.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
//Iteration until they meet match node.
var getIntersectionNode = function(headA, headB) {
    let valA = headA;
    let valB = headB;
    while(valA != valB) {
        valA = valA == null ? headA : valA.next;
        valB = valB == null ? headB : valB.next;
    }
    
    return valA;
    
};
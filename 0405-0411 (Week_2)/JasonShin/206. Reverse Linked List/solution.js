// https://leetcode.com/problems/reverse-linked-list/
// Monday submission

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// Recursive
var reverseListRecursive = function(head) {
    // Base case
    if(!head || !head.next) return head;
   
    let reverseLinkedList = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return reverseLinkedList;
    
    /*
    Reverse(3) [4(1xxx)-3-2-1-null]
    Reverse(4) [5(1x01)-4(1xxx)-null]
    Reverse(5) Return baseCase: [5-null]
    */
    //Time complexity: O(n)
    //Space complexity: O(n)
    
};
// //Iteration
var reverseListIteration = function(head){
    
    //Initial previous value.
    let prev = null;
    
    //In Iteration function.
    while(true){
        if(!head) break;
        let curr = head.next;
        head.next = prev
        prev = head;
        head = curr;
    }
    /*
        1st: prev: [1-null] head: [2-3-4-5-null]
        2nd: prev: [2-1-null] head: [3-4-5-null]
        3rd: prev: [3-2-1-null] head: [4-5-null]
    */
    
    return prev;
}
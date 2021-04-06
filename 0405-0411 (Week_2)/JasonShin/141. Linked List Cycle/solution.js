//https://leetcode.com/problems/linked-list-cycle/
//Tuesday Submission
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

 var hasCycle = function(head) {
    if(!head) return false;
    
    let fastPointer = head;
    let slowPointer = head;
    
    while(fastPointer){
        if(!fastPointer) return false;
        if(!fastPointer.next){
            return false;
        }
        else {
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }
        if(fastPointer === slowPointer) return true;
    }
    return false;
    
    
};
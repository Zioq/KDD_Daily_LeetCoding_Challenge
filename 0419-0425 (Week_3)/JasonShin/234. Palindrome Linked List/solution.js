// https://leetcode.com/problems/palindrome-linked-list/
// Wednesday Submission

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var isPalindrome = function(head) {
    let headVal = head;
    let normal = '';
    let reverse = '';
    
    while(headVal){
         normal += headVal.val;   
        headVal = headVal.next;
    }
    for(let i = normal.length-1; i>= 0; i--){
        reverse += normal[i];
    }
    
    if(normal === reverse){
        return true;
    } else {
        return false;
    }

    /**
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    
    
};
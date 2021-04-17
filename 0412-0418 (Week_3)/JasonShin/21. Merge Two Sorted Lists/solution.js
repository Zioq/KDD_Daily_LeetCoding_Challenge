// https://leetcode.com/problems/merge-two-sorted-lists/
// Thursday submission

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

//1st solution
 var mergeTwoLists = function(l1, l2) {
    let head, pointer;
    
    //If the other Linked list empty, the function just return 1 LikedList.
    if(!l1) {
        return l2;
    }
    if(!l2){
        return l1;
    }

    //Initial setup
    if(l1.val >= l2.val) {
        head = l2;
        pointer = l2;
        l2 = l2.next;
    } else {
        head = l1;
        pointer = l1;
        l1= l1.next;
    }

    while(true){
        //Break point
        if(!l1) {
            pointer.next = l2;
            break;
        }
        if(!l2) {
            pointer.next = l1;
            break;
        }
        
        //check the value
        if(l1.val <= l2.val){
            pointer.next = l1;
            l1 = l1.next;
        }else {
            pointer.next = l2;
            l2 = l2.next;
        }
        pointer = pointer.next;
    }
    
    return head;
};
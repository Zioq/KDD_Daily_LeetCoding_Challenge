/**
 2021-04-01 submission.


 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> ary = new ArrayList<Integer>();
        while(head != null){
            ary.add(head.val);
            head = head.next;   
        }
        Integer[] int_ary = new Integer[ary.size()];
        int_ary = ary.toArray(int_ary);
        for(int i = 0; i < int_ary.length/2; i++){
            if(int_ary[i] != int_ary[int_ary.length-i-1])
                return false;
        }
        return true;
    }
}

/ Submission for 2021-04-14
/**
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
    public ListNode partition(ListNode head, int x) {
        ListNode low_head = new ListNode(0);
        ListNode low = low_head;
        ListNode high_head = new ListNode(0);
        ListNode high = high_head;
        while(head != null){
            if(head.val < x){
                low.next = head;
                low = head;
            }
            else{
                high.next = head;
                high = head;
            }
            head = head.next;
        }
        high.next = null;
        low.next = high_head.next;
        return low_head.next;
    }
}

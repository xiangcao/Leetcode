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
    /**
     * Merge sort use bottom-up policy, 
     * so Space Complexity is O(1)
     * Time Complexity is O(NlgN)
     * stable sort
    */
    public ListNode sortList(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int n = 0;
        while (head != null) {
            head = head.next;
            n++;
        }
        for (int step = 1; step < n; step <<= 1) {
            ListNode prev = dummy;
            ListNode cur = dummy.next;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, step);
                cur = split(right, step);
                prev = merge(left, right, prev);
            } 
        }
        
        return dummy.next;
    }
    
    	/**
	 * Divide the linked list into two lists,
     * while the first list contains first n ndoes
	 * return the second list's head
	 */
    private ListNode split(ListNode head, int step) {
        if (head == null) return null;
    	
        for (int i = 1; head.next != null && i < step; i++) {
            head = head.next;
        }
        
        ListNode right = head.next;
        head.next = null;
        return right;
    }
    
    	/**
	  * merge the two sorted linked list l1 and l2,
	  * then append the merged sorted linked list to the node head
	  * return the tail of the merged sorted linked list
	 */
    private ListNode merge(ListNode left, ListNode right, ListNode prev) {
        ListNode cur = prev;
        while (left != null && right != null) {
            if (left.val < right.val) {
                cur.next = left;
                left = left.next;
            }
            else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        
        if (left != null) cur.next = left;
        else if (right != null) cur.next = right;
        while (cur.next != null) cur = cur.next;
        return cur;
    }
}

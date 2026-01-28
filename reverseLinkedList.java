public class reverseLinkedList {
    public static class ListNode {
     int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

    public  static ListNode reverseList(ListNode head) {
        ListNode currentNode = head;
        ListNode newHead = null;

        
        while(currentNode != null) {
            if(currentNode == head) {
                //initialise head
                newHead = new ListNode(currentNode.val, null);
            }
            else {   
            //create new node with value x and pointer to current head
                ListNode newNode = new ListNode(currentNode.val, newHead);
                //move head
                newHead = newNode;
            }
            
            //go to the next node
            currentNode = currentNode.next;
        }

        return newHead;
    }

    public static void main(String[] args) {

        ListNode node4 = new ListNode(4);
        ListNode node3 = new ListNode(3, node4);
        ListNode node2 = new ListNode(2, node3);
        ListNode head  = new ListNode(1, node2);
        
        System.out.print(reverseList(head).val);
        
    }
}

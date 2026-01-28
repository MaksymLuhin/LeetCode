public ListNode deleteDuplicates(ListNode head) {
        ListNode localHead = head;
        ListNode currentNode = head;

        while(currentNode != null && currentNode.next != null){
            if(currentNode.val == currentNode.next.val) {
                currentNode.next = currentNode.next.next;
            }

            if(currentNode.next == null) {
                break;
            }
            //check if the next value is different
            else if(currentNode.val != currentNode.next.val){
                currentNode = currentNode.next;
            }   
            else {
                continue;
            }
        }

        return localHead;
    }
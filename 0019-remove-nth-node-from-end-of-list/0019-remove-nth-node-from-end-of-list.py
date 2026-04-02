class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # 1. Advance fast pointer so there are n nodes between slow and fast
        for _ in range(n):
            if fast:
                fast = fast.next
        
        # 2. Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # 3. Skip the nth node
        slow.next = slow.next.next
        
        return dummy.next
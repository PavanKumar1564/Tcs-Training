def removeNthFromEnd(self, head, n):
        # https://leetcode.com/discuss/86721/o-n-solution-in-java
        if head is None:
            return None
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head
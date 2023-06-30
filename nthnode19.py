class Solution(object):
    def increment(self, n, right):
        k = 0
        while right.next:
            if k == n:
                break
            right = right.next
            k += 1
        return k, right

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # case when list is smaller than n

        # increment by n
        # if list smaller than n, do special modulo.
        left = head
        right = head

        k, right = self.increment(n + 1, right)

        if k < n:
            # k is length
            right = head
            k, right = self.increment(n % k + 1, right)
        # intermediate check
        print(right.val)

        # When the cut off is the last node.
        while right.next:
            left = left.next
            right = right.next

        left.next = right

        return head

        # then start incrementing with left and right until end

        #

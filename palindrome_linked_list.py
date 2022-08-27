from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node):
        node = ListNode(node)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        res = True
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        while head is not None:
            i = stack.pop()
            if i == head.val:
                res = True
            else:
                res = False
            head = head.next
        return res


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            current = head
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            head = prev
            return head

        def areidentical(l1, head):
            while (l1 and head):
                if l1.val != head.val:
                    return False
                l1 = l1.next
                head = head.next
            return True

        def copy_list(head):
            current = head
            dummy = ListNode()
            tail =dummy
            while current:
                tail.next = ListNode(current.val, tail.next)
                tail = tail.next
                current = current.next
            return dummy.next

        l1 = copy_list(head)
        l2 = reverse(head)

        return areidentical(l1, l2)



if __name__ == "__main__":
    l1 = [1,2,2,1]
    list1 = linkedList()
    for i in l1:
        list1.insert_node(i)
    res = Solution().isPalindrome(list1.head)
    res2 = Solution2().isPalindrome(list1.head)
    print(res)
    print(res2)
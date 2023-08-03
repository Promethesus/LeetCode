from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverse_linked_list(head:Optional[ListNode])->Optional[ListNode]: 
    current, previous = head, None

    while current:
        temp = current.next
        current.next = previous
        previous = current 
        current = temp

    return previous

print(reverse_linked_list([1,2,3,4,5]))
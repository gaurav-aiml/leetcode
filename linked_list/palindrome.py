# @author : Gaurav Pai
# date_created : 10/09/20
import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l1 = LinkedList(["a","b"])
print(l1)
def palindrome_ll(l1):
    rev = LinkedList()
    slow = l1.head
    fast = l1.head

    #slow and fast runner to find the middle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    #odd number of elements
    if fast is not None:
        slow = slow.next

    while slow is not None:
        rev.add_to_beginning(slow.data)
        slow = slow.next

    cur1 = l1.head
    cur2 = rev.head
    while cur2 is not None:
        if cur1.data != cur2.data:
            return False
        cur1 = cur1.next
        cur2 = cur2.next
    return True

print(palindrome_ll(l1))
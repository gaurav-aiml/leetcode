# @author : Gaurav Pai
# date_created : 10/09/20
import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l1 = LinkedList(["0", "a", "b", "c", "d", "e", "f"])
l2 = LinkedList(["b", "c", "d"])

cur = l1.head
for i in range(0):
    cur = cur.next
l2.tail.next = cur.next


def intersection(l1, l2):
    cur1 = l1.head
    cur2 = l2.head
    len1, len2 = 1, 1

    while cur1.next is not None:
        cur1 = cur1.next
        len1 += 1
    while cur2.next is not None:
        cur2 = cur2.next
        len2 += 1

    if cur1 != cur2:
        return "No Intersection"

    cur1 = l1.head
    cur2 = l2.head
    diff = len1 - len2
    if diff > 0:
        for i in range(diff):
            cur1 = cur1.next
    elif diff < 0:
        for i in range(abs(diff)):
            cur2 = cur2.next

    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1.data


# main function
print(intersection(l1, l2))

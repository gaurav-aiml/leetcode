# @author : Gaurav Pai
# date_created : 10/08/2

import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l = LinkedList([10, 14, 16,10,16,9,2,9,14,10])
print(l.___iterate__())


def remove_dups(l):
    current = l.head
    seen = set()
    seen.add(current.data)

    while current.next is not None:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return l

def remove_dups_hard(l):
    current = l.head
    while current.next is not None:
        iterator = current
        while iterator.next is not None:
            if iterator.next.data == current.data:
                iterator.next = iterator.next.next
            if iterator.next is None:
                break
            iterator = iterator.next
        current = current.next
    return l

remove_dups_hard(l)
print(l.___iterate__())



# @author : Gaurav Pai
# date_created : 10/08/2

import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l = LinkedList([5,6])
print(l.___iterate__())

def partition(l, d):
    cur = l.head
    swap = l.head
    while cur is not None and swap is not None:
        if cur.data >=d:
            while swap is not None:
                if swap.data >= d:
                    swap = swap.next
                else:
                    break
            if swap is not None:
                cur.data, swap.data = swap.data, cur.data
            else:
                break
        cur = cur.next
        swap = swap.next


partition(l,5)
print(l.___iterate__())

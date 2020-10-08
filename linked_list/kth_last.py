# @author : Gaurav Pai
# date_created : 10/08/2

import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l = LinkedList([10, 14, 16,10,16,9,2,9,14,10])
print(l.___iterate__())

def kth_from_last(l, k):
    # trivial
    # runner = l.head
    # length = 0
    #
    # if runner is None:
    #     return None
    #
    # while runner is not None:
    #     length += 1
    #     runner = runner.next
    #
    # if k > length - 1 :
    #     return None
    # if k == length - 1:
    #     return l.head.data
    # elif k == 0:
    #     return l.tail.data
    #
    # idx = length - k
    # runner = l.head
    # while runner is not None:
    #     idx -= 1
    #     if idx == 0:
    #         return runner.data
    #     runner = runner.next
    #
    return

def kth_from_last_recursive(n,k):
    if n is None:
        return -1
    index = kth_from_last_recursive(n.next, k) + 1
    if index == k:
        print(n.data)
    return index

kth_from_last_recursive(l.head, 1)
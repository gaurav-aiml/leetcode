# @author : Gaurav Pai
# date_created : 10/09/20

import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l1 = LinkedList([1, 0, 5, 0, 0])
l2 = LinkedList([6, 8, 5])

#reversed LL of numbers
def sum_lists(l1, l2):
    cur1 = l1.head
    cur2 = l2.head
    carry = 0
    l3 = LinkedList()
    while (cur1 is not None and cur2 is not None):
        res = carry + cur1.data + cur2.data
        carry = 0
        if res >= 10:
            carry = 1
            res %= 10
        l3.add(res)
        cur1 = cur1.next
        cur2 = cur2.next

    while cur1 is not None:
        res = carry + cur1.data
        carry = 0
        if res >= 10:
            res %= 10
            carry = 1
        l3.add(res)

        cur1 = cur1.next

    while cur2 is not None:
        res = carry + cur2.data
        carry = 0
        if res >= 10:
            res %= 10
            carry = 1

        l3.add(res)
        cur2 = cur2.next

    return l3

#follow up normal LL of numbers
def calculate_sum(n1, n2, l3):
    if n1 is None:
        return 0
    res = (calculate_sum(n1.next, n2.next, l3) + n1.data + n2.data)
    l3.add_to_beginning(res % 10)
    return int(res >= 10)
def sum_lists_rec(l1, l2):
    diff = len(l1) - len(l2)
    if diff != 0:
        if diff > 0:
            for i in range(diff):
                l2.add_to_beginning(0)
        else:
            for i in range(abs(diff)):
                l1.add_to_beginning(0)
    print(l1)
    print(l2)

    n1 = l1.head
    n2 = l2.head
    l3 = LinkedList()
    res = (calculate_sum(n1.next, n2.next, l3) + n1.data + n2.data)
    l3.add_to_beginning(res % 10)
    if res >= 10:
        l3.add_to_beginning(1)
    return l3


print(sum_lists_rec(l1, l2))

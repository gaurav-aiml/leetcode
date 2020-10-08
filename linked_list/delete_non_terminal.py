import sys

sys.path.append("..")
from linked_list.linkedlist import LinkedList

l = LinkedList([10, 14, 16,10,16,9,2,9,14,10])
print(l.___iterate__())

def delete_node(n):
    if n.next is None:
        return
    while n.next.next is not None:
        n.data = n.next.data
        n = n.next
    n.data = n.next.data
    n.next = None

cnt = 3
runner = l.head
while(cnt != 1):
    cnt -= 1
    runner = runner.next


delete_node(runner)
print(l.___iterate__())



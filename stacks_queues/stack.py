import sys
sys.path.append("..")
from linked_list.linkedlist import LinkedList


class Stack:

    def __init__(self):
        self.llist = LinkedList()

    def push(self, item):
        self.llist.add_to_beginning(item)

    def peek(self):
        return self.llist.head.data

    def pop(self):
        if self.llist.head is not None:
            n = self.llist.head.data
            self.llist.delete_from_beginning()
            return n
        else:
            return "Stack Empty Cannot Pop"

    def head(self):
        return self.llist.head
    def __iter__(self):
        return self.llist.___iter__()

    def __str__(self):
        return self.llist.__str__()

    def __len__(self):
        return self.llist.__len__()
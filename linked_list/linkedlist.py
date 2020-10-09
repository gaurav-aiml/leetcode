#@author : Gaurav Pai
#date-created : 10/08/20

class Node():
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data:
            self.add_multiple(data)

    def __len__(self):
        if self.head is None:
            return 0
        else:
            cnt = 0
            n = self.head
            while n is not None:
                cnt += 1
                n = n.next
            return cnt

    def __str__(self):
        values = [str(x) for x in self.___iterate__()]
        return ' -> '.join(values)

    def add_to_beginning(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            n = Node(data, self.head)
            self.head = n

    def add(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def ___iterate__(self):
        if self.head is None:
            return []
        n = self.head
        l = []
        while n is not None:
            l.append(n.data)
            n = n.next
        return l

    def add_multiple(self, data):
        for d in data:
            self.add(d)

    def delete_node(self,data):
        if self.head is None:
            return
        n = self.head

        while n.next.data != data:
            n = n.next

        n.next = n.next.next
        n.next.next = None

    def delete_from_end(self):
        if self.head is None:
            return

        n = self.head
        while(n.next is not None):
            n = n.next
        n.next = None
        self.tail = n

    def delete_from_beginning(self):
        if self.head is None:
            return

        self.head = self.head.next
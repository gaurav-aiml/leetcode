import sys
sys.path.append("..")

from stacks_queues.stack import Stack

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        if len(self.s1) == 0:
            self.s1.push(item)
        else:
            l = len(self.s1)

            for i in range(l):
                self.s2.push(self.s1.pop())
            self.s1.push(item)

            for i in range(l):
                self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def poll(self):
        return self.s1.peek()

    def __str__(self):
        return self.s1.__str__()


q = Queue()

for i in range(10):
    q.enqueue(i+1)

print(q)
for i in range(3):
    q.dequeue()

print(q)
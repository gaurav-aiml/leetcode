import sys
sys.path.append("..")
from stacks_queues.stack import Stack


class SetOfStacks:
    def __init__(self, threshold = 10):
        self.slist = [Stack()]
        self.cur = 0
        self.threshold = threshold

    def push(self, item):
        if len(self.slist[self.cur]) == self.threshold:
            self.cur += 1
            s = Stack()
            s.push(item)
            self.slist.append(s)
        else:
            self.slist[self.cur].push(item)

    def pop(self):
        if self.slist[self.cur].head() is None:
            self.cur -= 1
            self.slist = self.slist[:-1]

        if len(self.slist) > 0:
            return self.slist[self.cur].pop()

    def __str__(self):
        for i,s in enumerate(self.slist):
            print(s.__str__())

        return ""

main = SetOfStacks(threshold=5)

for i in range(12):
    main.push(i)

# print(main)


for i in range(13):
    main.pop()

print(main)
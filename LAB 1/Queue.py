class Stack:
    def __init__(self):
        self.elements = []

    def push(self, items):
        self.elements.append(items)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, items):
        self.in_stack.push(items)

    def dequeue(self):
        if self.out_stack.isEmpty:
            while self.in_stack.size() > 0:
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.elements.pop()


if __name__ == '__main__':
    q = Queue()

    for i in range (5):
        q.enqueue(i)

    for i in range (5):
        print(q.dequeue())
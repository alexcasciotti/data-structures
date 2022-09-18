class Stack:
    def __init__(self):
        self.stk = []
    def push(self, value):
        self.stk.append(value)
    def pop(self):
        to_remove = self.stk[len(self.stk) - 1]
        self.stk.remove(to_remove)
        return to_remove
    def peek(self):
        return self.stk[len(self.stk) - 1]
    def isEmpty(self):
        return len(self.stk) == 0

class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, value):
        self.q.append(value)
    def dequeue(self):
        to_remove = self.q[0]
        self.q.remove(to_remove)
        return to_remove
    def peek(self):
        return self.q[0]
    def isEmpty(self):
        return len(self.q) == 0





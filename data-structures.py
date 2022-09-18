class Stack:
    def __init__(self):
        self.stk = []
        self.top = -1
        self.size = 0
    def push(self, value):
        self.stk.append(value)
        self.top += 1
        self.size += 1
    def pop(self):
        self.top -= 1
        self.size -= 1
        return self.stk[self.top + 1]
    def peek(self):
        return self.stk[self.top]
    def isEmpty(self):
        return self.size == 0

# stk = Stack()
# stk.push(4)
# print(stk.peek())
# stk.push(3)
# print(stk.peek())
# stk.push(5)
# print(stk.peek())
# while(not stk.isEmpty()):
#     print(stk.pop())

class Queue:
    pass



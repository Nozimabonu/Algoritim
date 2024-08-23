# Class Stack --> append, pop, list
from collections import deque
from typing import Any


# Stack => push, pop, peek, is_empty, size
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        raise Exception('Stack is empty')

    def peek(self) -> Any:
        if not self.is_empty():
            return self.stack[-1]
        raise Exception('Stack is empty')

    def size(self) -> int:
        return len(self.stack)


stack = Stack()
stack.push('ali')
stack.push('malik')
stack.push('muhammad')
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.peek())
print(stack.size())

arr = deque

arr.appendleft(10)
arr.appendleft(20)
arr.appendleft(30)
print(arr)


# Queue => dequeue, enqueue

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        raise Exception('Queue is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise Exception('Queue is empty')

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
print(queue.is_empty())


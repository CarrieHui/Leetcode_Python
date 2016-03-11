# coding:utf-8

# https://leetcode.com/problems/implement-stack-using-queues/ (225. Implement Stack using Queues)

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack.size() == 0:
            return None
        else:
            tmpQueue = Queue()
            while self.stack.size() > 1:
                tmpQueue.push(self.stack.pop())
            self.stack.pop()
            while tmpQueue.size() > 0:
                self.stack.push(tmpQueue.pop())

    def top(self):
        """
        :rtype: int
        """
        if self.stack.size() == 0:
            return None
        else:
            tmpQueue = Queue()
            while self.stack.size() > 1:
                tmpQueue.push(self.stack.pop())
            ret = self.stack.peek()
            tmpQueue.push(self.stack.pop())
            while tmpQueue.size() > 0:
                self.stack.push(tmpQueue.pop())
            return ret

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack.size() == 0:
            return True
        else:
            return False

class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.size(self.queue) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    stk = Stack()
    print stk.empty()

    stk.push(1)
    stk.push(2)
    print stk.top()
    print stk.empty()

    stk.push(3)
    stk.push(4)
    print stk.top()

    stk.pop()
    stk.pop()
    stk.pop()
    print stk.top()
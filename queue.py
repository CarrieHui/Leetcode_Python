# coding:utf-8

# https://leetcode.com/problems/implement-queue-using-stacks/ (232. Implement Queue using Stacks)

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = MyStack()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue.size() == 0:
            pass
        else:
            tmpStack = MyStack()
            while self.queue.size() > 1:
                tmpStack.push(self.queue.pop())
            self.queue.pop()
            while tmpStack.size() > 0:
                self.queue.push(tmpStack.pop())

    def peek(self):
        """
        :rtype: int
        """
        if self.queue.size() == 0:
            return None
        else:
            tmpStack = MyStack()
            while self.queue.size() > 1:
                tmpStack.push(self.queue.pop())
            ret = self.queue.peek()
            while tmpStack.size() > 0:
                self.queue.push(tmpStack.pop())
            return ret

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue.size() == 0:
            return True
        else:
            return False


class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    print queue.peek()
    queue.push(3)
    print queue.peek()

    print queue.empty()

    queue.pop()
    print queue.peek()
    queue.pop()
    print queue.peek()
    queue.pop()

    print queue.empty()

class Queue:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def remove(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def getSize(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]


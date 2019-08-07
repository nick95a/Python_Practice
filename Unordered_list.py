class Node:

    def __init__(self, initInfo):
        self.info = initInfo
        self.next = None

    def set_info(self, info):
        self.info = info
        return "Request completed"

    def set_next(self, next):
        self.next = next
        return "Request completed"

    def get_info(self):
        return self.info

    def get_next(self):
        return self.next


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, info):
        t = Node(info)
        t.set_next(self.head)
        self.head = t

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.get_info() == item:
                found = True
            else:
                prev = current
                current = current.get_next()
        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            count += 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while not found and current != None
            if current.get_info() == item:
                found = True
            else:
                current = current.get_next()
        return found
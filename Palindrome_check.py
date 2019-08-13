class Deque:
    '''
    Deque class based on the built-in list datatype in Python
    '''
    def __init__(self):
        '''
        Creates an empty container in the form of a list
        '''
        self.deque = []

    def pushBack(self, item):
        '''
        The method pushes the item argument provided to the back of the deque
        :param item:
        :return:
        '''
        self.deque.append(item)

    def pushFront(self, item):
        '''
        The method pushes the item argument provided to the front of the deque.
        This is peculiar to the deque ADT and distinguishes it from the queue for example
        :param item:
        :return:
        '''
        self.deque.insert(0, item)

    def popBack(self):
        '''
        The method removes an item from the back of the deque.
        :return:
        '''
        return self.deque.pop()

    def popFront(self):
        '''
        The method removes an item from the front of the deque.
        :return:
        '''
        return self.deque.pop(0)

    def isEmpty(self):
        '''
        Method checks where the existing deque is empty.
        :return:
        '''
        return len(self.deque) == 0

    def getSize(self):
        '''
        Method returns the number of items present in the deque.
        :return:
        '''
        return len(self.deque)





def palin_check(item):
    equal = True
    d = Deque()
    for c in item:
        d.pushBack(c)
    if d.getSize() == 0:
        return False
    elif d.getSize() == 1:
        return True
    else:
        while equal and d.getSize() > 1:
            if d.popBack() != d.popFront():
                equal = False
        return equal

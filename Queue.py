class Queue:
    
    '''
    Queue ADT is implemented below based on the standard list data type in Python
    '''
    def __init__(self):
        '''
        The queue is initialized with an empty list
        '''
        self.queue = []

    def push(self, item):
        '''
        Appends an item at the end of the queue
        '''
        self.queue.append(item)

    def remove(self):
        '''
        Removes an element that is currently in 0 position in the queue
        '''
        return self.queue.pop(0)

    def isEmpty(self):
        '''
        Checks if the queue is empty
        '''
        return True if len(self.queue) == 0 else False

    def getSize(self):
        '''
        Returns the size of the queue
        '''
        return len(self.queue)

    def peek(self):
        '''
        Shows the first element in the queue
        '''
        return self.queue[0]


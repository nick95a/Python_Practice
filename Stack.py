class Stack:
    '''
    Stack ADT is built on the standard list datatype in Python
    '''
    def __init__(self):
        '''
        Initializes the stack in the form of an empty Python list
        '''
        self.stack = []

    def pop(self):
        '''
        Removes and returns the last element from the Stack
        :return:
        '''
        return self.stack.pop()

    def push(self, item):
        '''
        Adds an element to the top of the Stack
        :param item:
        :return:
        '''
        self.stack.append(item)

    def isEmpty(self):
        '''
        Checks if the stack has any elements
        :return:
        '''
        return True if len(self.stack) == 0 else False

    def getSize(self):
        '''
        Returns the size of the stack
        :return:
        '''
        return len(self.stack)

    def peek(self):
        '''
        Shows the top elements in the stack. Useful to know which element can be removed of the top of the stack
        :return:
        '''
        return self.stack[-1]


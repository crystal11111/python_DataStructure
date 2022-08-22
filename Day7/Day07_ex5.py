class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):


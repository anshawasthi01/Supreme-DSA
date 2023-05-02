class CirQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.front = -1
        self.rear = -1

    def push(self, data):
        # Queue Full

        # Single element case - first element

        # Circular nature

        # Normal flow
        # TODo: add one more condition in the QUEUE FULL if block
        if (self.front == 0 and self.rear == self.size - 1):
            print("Q is full, cannot insert")
        elif self.front == -1:
            self.front = self.rear = 0
            self.arr[self.rear] = data
        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.arr[self.rear] = data
        else:
            self.rear += 1
            self.arr[self.rear] = data

    def pop(self):
        # Empty check
        # Single element
        # Circular nature
        # Normal flow
        if self.front == -1:
            print("Q is empty, cannot pop")
        elif self.front == self.rear:
            self.arr[self.front] = -1
            self.front = -1
            self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

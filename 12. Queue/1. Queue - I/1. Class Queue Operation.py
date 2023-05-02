class Queue:
    def __init__(self, size):
        self.arr = [-1] * size
        self.size = size
        self.front = 0
        self.rear = 0
    
    def push(self, data):
        if self.rear == self.size:
            print("Q is full")
        else:
            self.arr[self.rear] = data
            self.rear += 1
    
    def pop(self):
        if self.front == self.rear:
            print("Q is empty")
        else:
            self.arr[self.front] = -1
            self.front += 1
            if self.front == self.rear:
                self.front = 0
                self.rear = 0
    
    def getFront(self):
        if self.front == self.rear:
            print("Q is empty")
            return -1
        else:
            return self.arr[self.front]
    
    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    
    def getSize(self):
        return self.rear - self.front

if __name__ == '__main__':
    q = Queue(10)

    q.push(5)
    q.push(15)
    q.push(25)
    q.push(55)

    print("Size of queue is:", q.getSize())

    q.pop()

    print("Size of queue is:", q.getSize())

    print("Front element is:", q.getFront())

    if q.isEmpty():
        print("Q is empty")
    else:
        print("Q is not empty")

class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1
        self.size = size

    def push(self, data):
        if self.top < self.size - 1:
            self.top += 1
            self.arr[self.top] = data
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top == -1:
            print("Stack underflow, can't delete element")
        else:
            self.top -= 1

    def get_top(self):
        if self.top == -1:
            print("There is no element in Stack")
        else:
            return self.arr[self.top]

    def get_size(self):
        return self.top + 1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

#CREATION
s = Stack(5)

#insertion
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

while not s.is_empty():
    print(s.get_top(), end=" ")
    s.pop()
print()

print("Size of stack: ", s.get_size())

s.pop()

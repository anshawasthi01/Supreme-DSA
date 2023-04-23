class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.size = size
        self.top1 = -1
        self.top2 = size

    def push1(self, data):
        if self.top2 - self.top1 == 1:
            # space not available
            print("OVERFLOW in stack 1")
        else:
            # space available
            self.top1 += 1
            self.arr[self.top1] = data

    def pop1(self):
        if self.top1 == -1:
            # stack empty
            print("UNDERFLOW in stack 1")
        else:
            # stack not empty
            self.arr[self.top1] = 0
            self.top1 -= 1

    def push2(self, data):
        if self.top2 - self.top1 == 1:
            # space not available
            print("OVERFLOW in stack 2")
        else:
            self.top2 -= 1
            self.arr[self.top2] = data

    def pop2(self):
        if self.top2 == self.size:
            # stack 2 is empty
            print("UNDERFLOW in stack 2")
        else:
            # stack 2 is not empty
            self.arr[self.top2] = 0
            self.top2 += 1

    def print(self):
        print(f"top1: {self.top1}")
        print(f"top2: {self.top2}")
        # print(" ".join(str(val) for val in self.arr))
        for i in range(self.size):
            print(self.arr[i], " ")
        print()


s = Stack(10)

s.push1(10)
s.print()
s.push1(20)
s.print()
s.push1(30)
s.print()
s.push1(40)
s.print()
s.push1(50)
s.print()

s.push2(100)
s.print()
s.push2(110)
s.print()
s.push2(120)
s.print()
s.push2(130)
s.print()
s.push2(140)
s.print()

s.pop1()
s.print()
s.pop1()
s.print()
s.pop1()
s.print()
s.pop1()
s.print()
s.pop1()
s.print()

s.push2(1000)
s.print()
s.pop1()
s.print()

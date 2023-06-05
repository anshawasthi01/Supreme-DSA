class NStack:
    def __init__(self, n, size):
        self.n = n  # Number of stacks
        self.size = size  # Size of main array
        self.freeSpot = 0  # Represents free space in the main array
        self.a = [0] * size
        self.top = [-1] * n
        self.next = [i + 1 for i in range(size)]
        self.next[size - 1] = -1

    def push(self, X, m):
        if self.freeSpot == -1:
            return False  # Stack overflow

        # 1. Find index
        index = self.freeSpot  

        # 2. Update freeSpot
        self.freeSpot = self.next[index]  

        # 3. Insert
        self.a[index] = X  

        # 4. Update next
        self.next[index] = self.top[m - 1]  

        # 5. Update top
        self.top[m - 1] = index  

        return True  # Push success

    # pop from mth stack
    def pop(self, m):
        if self.top[m - 1] == -1:
            return -1  # Stack underflow

        index = self.top[m - 1]
        self.top[m - 1] = self.next[index]
        poppedElement = self.a[index]
        self.next[index] = self.freeSpot
        self.freeSpot = index

        return poppedElement

    def __del__(self):
        del self.a
        del self.top
        del self.next


s = NStack(3, 6)
print(s.push(10, 1))
print(s.push(10, 1))
print(s.push(10, 1))
print(s.push(14, 2))
print(s.push(15, 3))
print(s.pop(1))
print(s.pop(2))

class Heap:
    def __init__(self):
        self.arr = [0] * 101
        self.size = 0
    
    def insert(self, value):
        # value insert karo end me
        self.size += 1
        index = self.size
        self.arr[index] = value

        # iss value ko place at right{correct position} position
        while index > 1:
            parentIndex = index // 2
            if self.arr[index] > self.arr[parentIndex]:
                self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
                index = parentIndex
            else:
                break
    
    def delete(self):
        ans = self.arr[1]
        # replace root node value with last node data
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        
        # place root node ka data on its correct position
        index = 1
        while index <= self.size:
            left = 2 * index
            right = 2 * index + 1
            
            largest = index
            if left <= self.size and self.arr[largest] < self.arr[left]:
                largest = left
            if right <= self.size and self.arr[largest] < self.arr[right]:
                largest = right
            
            if largest == index:
                break
            else:
                self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
                index = largest
        
        return ans


h = Heap()
# h.arr[0] = -1
# h.arr[1] = 100
# h.arr[2] = 50
# h.arr[3] = 60
# h.arr[4] = 40
# h.arr[5] = 45
# h.size = 5
h.insert(50)
h.insert(30)
h.insert(70)
h.insert(40)
h.insert(80)
h.insert(100)

print("Printing the heap:")
for i in range(1, h.size + 1):
    print(h.arr[i], end=" ")
print()

h.insert(110)
print("Printing the heap")
for i in range(h.size+1):
    print(h.arr[i]," ")
print()

# Example of deleting the root
deleted_value = h.delete()
print("Deleted value:", deleted_value)

print("Printing the updated heap:")
for i in range(1, h.size + 1):
    print(h.arr[i], end=" ")
print()

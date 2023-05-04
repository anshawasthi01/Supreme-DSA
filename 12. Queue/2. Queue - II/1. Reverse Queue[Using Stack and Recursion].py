from queue import Queue

def reverseQueue(q: Queue[int]) -> None:
    s = []

    # Step 1: Put all elements of q into s
    while not q.empty():
        element = q.get()
        s.append(element)

    # Step 2: Put all elements from stack into q
    while s:
        element = s.pop()
        q.put(element)

def reverseQueueRecursion(q: Queue[int]) -> None:
    # Base case
    if q.empty():
        return

    # Step A
    temp = q.get()

    # Step B
    reverseQueueRecursion(q)

    # Step C
    q.put(temp)

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

reverseQueue(q)

print("Printing Queue after reversing:")
while not q.empty():
    print(q.get(), end=" ")

print("\n")

q.put(1)
q.put(2)
q.put(3)
q.put(4)

reverseQueueRecursion(q)

print("Printing Queue after reversing recursively:")
while not q.empty():
    print(q.get(), end=" ")

print("\n")

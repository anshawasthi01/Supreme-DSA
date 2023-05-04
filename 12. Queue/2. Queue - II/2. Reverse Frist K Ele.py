from queue import Queue

def reverseK(q: Queue[int], k: int) -> None:
    # Step A: queue -> k elements -> stack
    s = []
    count = 0
    n = q.qsize()

    if k <= 0 or k > n:
        return

    while not q.empty():
        temp = q.get()
        s.append(temp)
        count += 1

        if count == k:
            break

    # Step B: stack -> q me qapas
    while s:
        temp = s.pop()
        q.put(temp)

    # Step C: push n-k element from q front to back
    count = 0
    while not q.empty() and n - k != 0:
        temp = q.get()
        q.put(temp)
        count += 1

        if count == n - k:
            break

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

k = 3
reverseK(q, k)

print("Printing Queue after reversing k elements from front:")
while not q.empty():
    print(q.get(), end=" ")

print("\n")

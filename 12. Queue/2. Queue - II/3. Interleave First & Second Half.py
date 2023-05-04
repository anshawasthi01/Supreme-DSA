from queue import Queue

def interleaveQueue(q: Queue[int]) -> None:
    # Step A: separate both halves
    n = q.qsize()
    if q.empty():
        return
    k = n // 2
    count = 0
    q2 = Queue()

    while not q.empty():
        temp = q.get()
        q2.put(temp)
        count += 1

        if count == k:
            break

    # Step B: interleaving start krdo
    while not q.empty() and not q2.empty():
        first = q2.get()
        q.put(first)

        second = q.get()
        q.put(second)

    # odd wala case
    if n & 1:
        element = q.get()
        q.put(element)

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(7)
q.put(8)
q.put(9)

interleaveQueue(q)

print("Printing Queue after interleave:")
while not q.empty():
    print(q.get(), end=" ")

print("\n")

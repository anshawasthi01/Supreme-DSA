from queue import Queue

# creation
q = Queue()

# insertion
q.put(5)
q.put(15)
q.put(25)
q.put(55)

# size
print("Size of queue is: ", q.qsize())

# removal
q.get()

print("Size of queue is: ", q.qsize())

if q.empty():
    print("Q is empty")
else:
    print("Q is not empty")

print("Front element is: ", q.queue[0])

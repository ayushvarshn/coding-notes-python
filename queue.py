# There are two queues in python collections.deque and queue.Queue

#collections.deque, a doubly ended queue. Can be used as stack/queue.

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')

print(q.popleft())


# queue.Queue

from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')


print(q.get())

print("Empty: ", q.empty()) 
print("Full: ", q.full())

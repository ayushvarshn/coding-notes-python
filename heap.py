# The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). Whenever elements are pushed or popped, heap structure is maintained. 
# The heap[0] element also returns the smallest element each time. Let’s see various Operations on the heap in Python.

import heapq

# initializing list
elems = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(elems)

heapq.heappush(elems, 4)
heapq.heappop(elems)


# To create a comparator. Now when adding Node to heap, it will act as as a max heap
class Node(object):
    def __init__(self, val: int):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

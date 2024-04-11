# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

class EvenNumbers:

  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __next__(self):
    if self.start >= self.end:
      raise StopIteration
    self.start = self.start + 2
    return self.start

  def __iter__(self):
    return self


# To run the Iterator
evenNums = EvenNumbers(2,20)
for x in evenNums:
    print(x)

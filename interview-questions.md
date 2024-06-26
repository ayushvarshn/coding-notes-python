**Can dict have immutable keys?**
No, Dict can't have immutable keys. Can only have mutable keys.
e.g. tuples can be used as keys while list can't be

**What is GIL?**
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.
(i.e. only one thread can be in a state of execution at any point in time)

**How reference count works?**
Python uses reference counting for memory management. 
It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. 
When this count reaches zero, the memory occupied by the object is released.

**How do you define access modifiers?**
_ means protected. __ means private.
They can be accessed anywhere but it is not recommended to access them outside.
```
class c1:
    def __init__(self,a,b,c):
        self.public=a
        self._protected=b
        self.__private=c
```
**Row-major order vs. column major order?** In row-major order, row-vectors  are stored in contiguous memory locations. And in column-major order, column-vectors are stored in contiguous memory locations. Since it’s faster to read and write data that’s stored in contiguous memory, rows operations are faster on row-major order matrices columns operations run faster on column-major order matrices.
```
column-major : Pandas 
row-major memory layout : C, C++, Java, Python, NumPy 
```

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

**Why numpy is faster than pandas?** 

* Optimized for Numerical Computations: NumPy is designed specifically for numerical computation, utilizing efficient data structures and algorithms tailored for such tasks.

* Homogeneous Data: NumPy arrays store data of the same type, which allows for more efficient memory usage and operations. Pandas DataFrames, on the other hand, can store mixed data types, which adds overhead.

* Vectorized Operations: NumPy supports vectorized operations, which means that operations are applied element-wise on arrays without the need for explicit loops. This takes advantage of low-level optimizations and can be executed much faster.

* Lower-Level Operations: NumPy operations are implemented in C, and they interface directly with low-level memory management, leading to significant performance improvements over the higher-level abstractions in Pandas.

* Reduced Overhead: Pandas provides more functionality and flexibility for data manipulation and analysis, which comes with additional overhead. This makes it slower for tasks where these additional features are not necessary.

**Python Memory Management**

**Heap Memory**
* Heap memory is used for dynamic memory allocation. This includes objects like lists, dictionaries, and class instances, which are created and managed at runtime.
* Heap memory is managed through Python’s memory manager and garbage collector. Python uses a combination of reference counting and generational garbage collection to handle the lifecycle of objects and reclaim memory when objects are no longer needed.
* Python uses memory pools and arenas to manage heap memory efficiently. Objects are allocated in fixed-size blocks from these pools, which helps reduce fragmentation and improve performance.

**Stack Memory**
* Stack memory is used for managing function calls and local variables. Each time a function is called, a new stack frame is created to hold the function’s local variables, arguments, and return address.

**How Memory Pools Work in Python**
PyMalloc:
PyMalloc is Python's specialized allocator for small objects. It uses a system of memory pools to manage memory efficiently.
PyMalloc organizes memory into different pools based on the size of the objects being allocated. Each pool is a collection of memory blocks of a specific size.

Object Allocation:
When an object is created, Python’s memory manager allocates memory from the appropriate pool based on the object’s size. For example, objects that fit into a small block size are allocated from a pool dedicated to small objects.

Object Deallocation:
When an object is no longer needed, its memory is returned to the pool rather than being freed back to the operating system. This memory can then be reused for future allocations, reducing the overhead of repeated allocations and deallocations.

Memory Arenas:
Arenas are large blocks of memory that are divided into smaller pools. Python allocates and manages memory in these arenas to handle large numbers of small objects efficiently.

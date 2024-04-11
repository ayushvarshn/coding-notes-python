# Threading 
# In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). 
# If you want your application to make better use of the computational resources of multi-core machines, you are advised to use multiprocessing or concurrent.futures.ProcessPoolExecutor. 
# However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.
# A daemon thread will shut down immediately when the program exits. One way to think about these definitions is to consider the daemon thread a thread that runs in the background without worrying about shutting it down.
# If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. 
# Threads that are daemons, however, are just killed wherever they are when the program is exiting.

def withdraw(balance, index):
    for _ in range(100000):
        balance[index]= balance[index] - 1 
    return balance

def deposit(balance, index):
    for _ in range(100000):
        balance[index] = balance[index] + 1
    return balance

balance = [100]

import threading

t1 = threading.Thread(target = withdraw, args= (balance, 0))
t2 = threading.Thread(target = deposit, args= (balance, 0))

t1.start()
t2.start()

t1.join()
t2.join()

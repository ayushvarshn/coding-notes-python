def withdraw(balance, index, lock):
    for _ in range(100000):
        lock.acquire()
        balance[index]= balance[index] - 1 
        lock.release()
    return balance

def deposit(balance, index,lock):
    for _ in range(100000):
        lock.acquire()
        balance[index] = balance[index] + 1
        lock.release()
    return balance

balance = [100]

import threading
lock = threading.Lock()
t1 = threading.Thread(target=withdraw,args=(balance, 0, lock))
t2 = threading.Thread(target=deposit,args=(balance, 0, lock))

t1.start()
t2.start()

t1.join()
t2.join()

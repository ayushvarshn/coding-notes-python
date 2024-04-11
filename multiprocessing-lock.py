# multiprocessing.Lock

import multiprocessing

def withdraw(balance, lock):
    for _ in range(100000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()
    return balance

def deposit(balance, lock):
    for _ in range(100000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()
    return balance

def perform_transaction():
    balance =  multiprocessing.Value('i',100)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit,args=(balance,lock))
    p2 = multiprocessing.Process(target=withdraw,args=(balance,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(balance.value)

if __name__ == "__main__":
    perform_transaction()
